#!/usr/bin/env python3
"""Reconstrói data/components.json e os wrappers em src/components/.

Plugins: busca os N mais baixados no repositório livre do wordpress.org
(action=query_plugins, browse=popular) e reordena localmente por `downloaded`
— mesmo critério usado na primeira montagem do catálogo (commit 8b9ef0a).
Entradas do JSON com `"pinned": true` (plugins fora do top-N mas relevantes por
outro motivo — ex.: citados no livro de segurança) sobrevivem à regeneração.

Temas: NÃO são regerados por popularidade — não há métrica pública de
downloads para temas equivalente à de plugins, e a lista atual mistura temas
padrão do WordPress com marcas premium mantidas de propósito (fora do
repositório livre, para deixar documentado o que falta cobrir). A lista de
temas do JSON existente é preservada como está; use --verify-themes para só
checar (sem alterar) se os slugs atuais ainda resolvem na API.

Depois de escrever o catálogo, regenera os wrappers de PLUGIN em
src/components/<slug>/download.py: cria os novos, atualiza os que mudaram de
nome/slug e remove os que saíram da lista. Wrappers de tema não são tocados
(a lista de temas não muda aqui).

Uso:
    python3 src/build_catalog.py                  # aplica (top 200 plugins)
    python3 src/build_catalog.py --limit 300       # outro tamanho
    python3 src/build_catalog.py --dry-run         # só mostra o que mudaria
    python3 src/build_catalog.py --verify-themes   # também audita slugs de tema
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from downloader import load_env  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
COMPONENTS_JSON = REPO_ROOT / "data" / "components.json"
COMPONENTS_DIR = REPO_ROOT / "src" / "components"

USER_AGENT = "vulnerapress-catalog/0"


def _get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_top_plugins(limit: int) -> list[dict]:
    """Busca os `limit` plugins livres mais baixados.

    Pede um pool maior que `limit` via browse=popular (a ordem de "popular"
    não é estritamente por downloads) e reordena localmente, igual ao
    critério original do catálogo.
    """
    fetch_count = min(limit * 2, 400)
    params = {
        "action": "query_plugins",
        "request[browse]": "popular",
        "request[per_page]": str(fetch_count),
        "request[page]": "1",
        "request[fields][downloaded]": "1",
        "request[fields][active_installs]": "1",
        "request[fields][icons]": "0",
        "request[fields][sections]": "0",
        "request[fields][description]": "0",
        "request[fields][short_description]": "0",
    }
    url = "https://api.wordpress.org/plugins/info/1.2/?" + urllib.parse.urlencode(params)
    data = _get_json(url)
    plugins = data.get("plugins", [])
    if not plugins:
        raise RuntimeError("API de plugins não retornou nada — abortando sem tocar no catálogo.")

    ranked = sorted(plugins, key=lambda p: p.get("downloaded", 0), reverse=True)[:limit]
    return [
        {
            "name": p["name"],
            "slug": p["slug"],
            "downloaded": p.get("downloaded", 0),
            "active_installs": p.get("active_installs", 0),
        }
        for p in ranked
    ]


def verify_theme_slugs(themes: list[dict], sleep_seconds: float) -> None:
    """Audita (sem alterar) se cada slug de tema resolve na API. Só reporta."""
    for i, theme in enumerate(themes):
        slug = theme["slug"]
        params = urllib.parse.urlencode({"action": "theme_information", "request[slug]": slug})
        url = f"https://api.wordpress.org/themes/info/1.1/?{params}"
        try:
            data = _get_json(url)
            version = data.get("version") if isinstance(data, dict) else None
        except Exception:
            version = None
        status = f"OK (v{version})" if version else "sem versão livre (esperado p/ premium)"
        print(f"  [tema] {theme['name']} ({slug}): {status}")
        if i < len(themes) - 1 and sleep_seconds > 0:
            time.sleep(sleep_seconds)


def diff_slugs(old: list[dict], new: list[dict]) -> tuple[set, set]:
    old_slugs = {c["slug"] for c in old}
    new_slugs = {c["slug"] for c in new}
    return new_slugs - old_slugs, old_slugs - new_slugs


def wrapper_source(name: str, slug: str, kind: str) -> str:
    component = repr({"name": name, "slug": slug, "type": kind})
    # repr() usa aspas simples e é determinístico o bastante p/ diffs estáveis.
    return f'''#!/usr/bin/env python3
"""Wrapper de download do componente: {name}."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {component}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
'''


def write_wrapper(name: str, slug: str, kind: str) -> None:
    d = COMPONENTS_DIR / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "download.py").write_text(wrapper_source(name, slug, kind), encoding="utf-8")


def remove_wrapper(slug: str) -> None:
    d = COMPONENTS_DIR / slug
    f = d / "download.py"
    if f.exists():
        f.unlink()
    try:
        d.rmdir()  # só remove se ficou vazio
    except OSError:
        pass


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=200, help="quantos plugins manter (default 200)")
    parser.add_argument("--dry-run", action="store_true", help="só mostra o que mudaria, não escreve nada")
    parser.add_argument("--verify-themes", action="store_true", help="audita slugs de tema contra a API (não altera)")
    args = parser.parse_args(argv[1:])

    load_env()
    old_catalog = json.loads(COMPONENTS_JSON.read_text("utf-8"))
    old_plugins = old_catalog.get("plugins", [])
    themes = old_catalog.get("themes", [])  # preservados como estão

    print(f"[…] buscando os {args.limit} plugins livres mais baixados…")
    new_plugins = fetch_top_plugins(args.limit)

    # Entradas com "pinned": true (ex.: plugins citados no livro de segurança, fora
    # do top-N por popularidade) sobrevivem à regeneração — mesma lógica usada para
    # preservar temas premium fora do repositório livre.
    new_slugs = {p["slug"] for p in new_plugins}
    pinned = [p for p in old_plugins if p.get("pinned") and p["slug"] not in new_slugs]
    new_plugins = new_plugins + pinned

    added, removed = diff_slugs(old_plugins, new_plugins)
    print(f"[i] plugins: {len(old_plugins)} -> {len(new_plugins)} | +{len(added)} novos, -{len(removed)} saíram")
    if added:
        print("    novos:", ", ".join(sorted(added)))
    if removed:
        print("    saíram:", ", ".join(sorted(removed)))

    if args.verify_themes:
        print(f"[…] auditando {len(themes)} slugs de tema (não altera nada)…")
        verify_theme_slugs(themes, sleep_seconds=3)

    if args.dry_run:
        print("[=] --dry-run: nada foi escrito.")
        return 0

    new_catalog = {"plugins": new_plugins, "themes": themes}
    COMPONENTS_JSON.write_text(
        json.dumps(new_catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"[✓] {COMPONENTS_JSON.relative_to(REPO_ROOT)} atualizado.")

    for p in new_plugins:
        write_wrapper(p["name"], p["slug"], "plugin")
    for slug in removed:
        remove_wrapper(slug)
    print(f"[✓] wrappers de plugin regenerados em {COMPONENTS_DIR.relative_to(REPO_ROOT)}/ "
          f"({len(added)} criados, {len(removed)} removidos).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
