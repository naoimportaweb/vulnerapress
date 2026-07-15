#!/usr/bin/env python3
"""Módulo compartilhado de download de componentes do Vulnerapress.

Fluxo (por componente):
  1. Descobre a versão no repositório oficial wordpress.org (via craudiowebot).
     - Se o componente não tiver versão conhecida, a "versão" passa a ser o
       md5 do próprio arquivo baixado.
  2. Monta o caminho no cofre: PATH_COFRE/<slug>/downloads/
  3. Se já existir o arquivo daquela versão no cofre, não baixa de novo
     (checagem por nome-de-versão + verificação de integridade por sha1).
  4. Se não existir: baixa via craudiowebot, salva no cofre e grava um
     sidecar .json com o MESMO nome do arquivo salvo + ".json".

Sem dependências externas: usa apenas a biblioteca padrão.

ATENÇÃO — craudiowebot: eu ainda não conheço os endpoints reais do bot na
porta 11015. Toda a comunicação está isolada na classe `Craudiowebot` abaixo,
com um contrato ASSUMIDO e totalmente configurável por variáveis de ambiente.
Ajuste `CRAUDIOWEBOT_*` (ou me passe a doc) para casar com a API real.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------- #
# Configuração / .env
# --------------------------------------------------------------------------- #

REPO_ROOT = Path(__file__).resolve().parents[1]  # raiz do projeto (contém .env)


def load_env(path: Path = REPO_ROOT / ".env") -> None:
    """Carrega pares KEY=VALUE do .env para os.environ (sem sobrescrever)."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def vault_root() -> Path:
    """Raiz do cofre (PATH_COFRE). Erra cedo se não estiver configurado."""
    load_env()
    raw = os.environ.get("PATH_COFRE")
    if not raw:
        raise RuntimeError("PATH_COFRE não definido (.env ou variável de ambiente).")
    return Path(raw).expanduser()


# --------------------------------------------------------------------------- #
# Fetchers (backends de download) — selecionáveis por FETCH_BACKEND
# --------------------------------------------------------------------------- #


class Fetcher:
    """Interface comum dos backends: get_bytes(url)->bytes; get_json(url)->dict."""

    def get_bytes(self, target_url: str) -> bytes:  # pragma: no cover
        raise NotImplementedError

    def get_json(self, target_url: str) -> dict:
        return json.loads(self.get_bytes(target_url).decode("utf-8"))


class Craudiowebot(Fetcher):
    """Cliente para o craudiowebot na porta 11015.

    Contrato assumido (mude via env se a API real for diferente):
        GET  http://{HOST}:{PORT}{FETCH_PATH}?{URL_PARAM}=<url-encoded>
        -> corpo da resposta = bytes crus do recurso navegado/baixado.

    Variáveis de ambiente:
        CRAUDIOWEBOT_HOST       (default 127.0.0.1)
        CRAUDIOWEBOT_PORT       (default 11015)
        CRAUDIOWEBOT_FETCH_PATH (default /fetch)
        CRAUDIOWEBOT_URL_PARAM  (default url)
        CRAUDIOWEBOT_TIMEOUT    (default 120 segundos)
        CRAUDIOWEBOT_DIRECT     (default 0) — fallback: busca a URL direto,
                                sem passar pelo bot. Use só para teste/quando
                                o craudiowebot estiver indisponível.
    """

    def __init__(self) -> None:
        load_env()
        self.host = os.environ.get("CRAUDIOWEBOT_HOST", "127.0.0.1")
        self.port = int(os.environ.get("CRAUDIOWEBOT_PORT", "11015"))
        self.fetch_path = os.environ.get("CRAUDIOWEBOT_FETCH_PATH", "/fetch")
        self.url_param = os.environ.get("CRAUDIOWEBOT_URL_PARAM", "url")
        self.timeout = int(os.environ.get("CRAUDIOWEBOT_TIMEOUT", "120"))
        self.direct = os.environ.get("CRAUDIOWEBOT_DIRECT", "0") not in ("", "0", "false")

    def _endpoint(self, target_url: str) -> str:
        query = urllib.parse.urlencode({self.url_param: target_url})
        return f"http://{self.host}:{self.port}{self.fetch_path}?{query}"

    def get_bytes(self, target_url: str) -> bytes:
        """Navega até `target_url` pelo bot e retorna os bytes crus.

        Em modo `direct` (fallback), busca a URL diretamente.
        """
        request_url = target_url if self.direct else self._endpoint(target_url)
        req = urllib.request.Request(
            request_url,
            headers={"Accept": "*/*", "User-Agent": "vulnerapress-downloader/0"},
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return resp.read()

# --------------------------------------------------------------------------- #
# Fetcher alternativo (PILOTO): HTTP direto via stdlib.
# Candidato a SUBSTITUIR o craudiowebot — sem serviço externo, sem dependências.
# --------------------------------------------------------------------------- #


class HttpFetcher(Fetcher):
    """Baixa direto por HTTP(S) com urllib. Backend do piloto de substituição."""

    def __init__(self) -> None:
        load_env()
        self.timeout = int(os.environ.get("FETCH_TIMEOUT", "120"))

    def get_bytes(self, target_url: str) -> bytes:
        req = urllib.request.Request(
            target_url,
            headers={"Accept": "*/*", "User-Agent": "vulnerapress-downloader/0"},
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return resp.read()


def make_fetcher() -> Fetcher:
    """Escolhe o backend por env FETCH_BACKEND: 'http' | 'craudiowebot' (default).

    'http' é o piloto candidato a substituir o craudiowebot. Compat: o antigo
    CRAUDIOWEBOT_DIRECT=1 também força o backend HTTP.
    """
    load_env()
    backend = os.environ.get("FETCH_BACKEND", "").strip().lower()
    direct = os.environ.get("CRAUDIOWEBOT_DIRECT", "0") not in ("", "0", "false")
    if backend == "http" or direct:
        return HttpFetcher()
    return Craudiowebot()


# --------------------------------------------------------------------------- #
# Metadados no repositório oficial wordpress.org
# --------------------------------------------------------------------------- #


def fetch_metadata(bot: Fetcher, slug: str, kind: str) -> dict | None:
    """Descobre versão e URL de download no repositório oficial.

    Retorna {"version": str, "download_url": str} ou None se o componente não
    estiver no repositório livre (típico dos premium: WP Rocket, Divi, etc.).

    NOTA: `slug` aqui é derivado do nome de exibição e pode NÃO coincidir com o
    slug canônico do wordpress.org (ex.: "solid-security-ithemes-security" no
    repositório é "better-wp-security"). Nesses casos o lookup retorna None.
    Para 100% de cobertura, adicione um `repo_slug` por componente no JSON.
    """
    if kind == "plugin":
        url = f"https://api.wordpress.org/plugins/info/1.0/{slug}.json"
    elif kind == "theme":
        params = urllib.parse.urlencode(
            {"action": "theme_information", "request[slug]": slug}
        )
        url = f"https://api.wordpress.org/themes/info/1.1/?{params}"
    else:
        raise ValueError(f"kind inválido: {kind!r}")

    try:
        data = bot.get_json(url)
    except Exception:
        return None

    if not isinstance(data, dict) or data.get("error") or not data.get("version"):
        return None
    if not data.get("download_link"):
        return None
    return {"version": data["version"], "download_url": data["download_link"]}


# --------------------------------------------------------------------------- #
# Hashes / caminhos no cofre
# --------------------------------------------------------------------------- #


def sha1_bytes(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def md5_bytes(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def sha1_file(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def downloads_dir(slug: str) -> Path:
    """PATH_COFRE/<slug>/downloads/ (criado se necessário)."""
    d = vault_root() / slug / "downloads"
    d.mkdir(parents=True, exist_ok=True)
    return d


def artifact_name(slug: str, version: str) -> str:
    """Nome do arquivo salvo, com a versão embutida."""
    safe_version = version.replace(os.sep, "_").replace(" ", "_")
    return f"{slug}-{safe_version}.zip"


# --------------------------------------------------------------------------- #
# Orquestração
# --------------------------------------------------------------------------- #


def sync_component(name: str, slug: str, type: str) -> int:  # noqa: A002
    """Sincroniza um componente com o cofre. Retorna 0 em sucesso.

    `type` deve ser "plugin" ou "theme".
    """
    bot = make_fetcher()
    dest_dir = downloads_dir(slug)

    meta = fetch_metadata(bot, slug, type)

    # --- Caminho A: versão conhecida no repositório --------------------------
    if meta is not None:
        version = meta["version"]
        download_url = meta["download_url"]
        filename = artifact_name(slug, version)
        target = dest_dir / filename
        sidecar = target.with_name(filename + ".json")

        if target.exists():
            # Já temos essa versão; confere integridade via sha1 do sidecar.
            expected = _sidecar_sha1(sidecar)
            if expected is None or sha1_file(target) == expected:
                print(f"[=] {name}: versão {version} já no cofre — pulando.")
                return 0
            print(f"[!] {name}: {filename} corrompido (sha1 difere), rebaixando.")

        print(f"[↓] {name}: baixando versão {version}…")
        content = bot.get_bytes(download_url)
        return _store(target, sidecar, content, name, slug, type, version, download_url)

    # --- Caminho B: sem versão no repositório -> versiona por md5 ------------
    # (esperado para premium/itens fora do repositório livre.)
    print(f"[?] {name}: sem versão livre no repositório oficial.")
    print(f"    Marque um repo_slug correto ou uma fonte licenciada. Pulando.")
    return 0


def _store(
    target: Path,
    sidecar: Path,
    content: bytes,
    name: str,
    slug: str,
    type: str,  # noqa: A002
    version: str,
    source_url: str,
) -> int:
    """Grava o artefato + sidecar .json. Deduplica por md5 quando aplicável."""
    digest_sha1 = sha1_bytes(content)
    digest_md5 = md5_bytes(content)

    target.write_bytes(content)
    metadata = {
        "name": name,
        "slug": slug,
        "type": type,
        "version": version,
        "source_url": source_url,
        "filename": target.name,
        "size_bytes": len(content),
        "sha1": digest_sha1,
        "md5": digest_md5,
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
    }
    sidecar.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), "utf-8")
    print(f"[✓] {name}: salvo {target.name} ({len(content)} bytes, sha1 {digest_sha1[:12]}…)")
    return 0


def _sidecar_sha1(sidecar: Path) -> str | None:
    if not sidecar.exists():
        return None
    try:
        return json.loads(sidecar.read_text("utf-8")).get("sha1")
    except Exception:
        return None


if __name__ == "__main__":
    # Uso: python downloader.py <slug> <plugin|theme> [nome]
    if len(sys.argv) < 3:
        print("uso: python downloader.py <slug> <plugin|theme> [nome]", file=sys.stderr)
        sys.exit(2)
    _slug, _type = sys.argv[1], sys.argv[2]
    _name = sys.argv[3] if len(sys.argv) > 3 else _slug
    sys.exit(sync_component(_name, _slug, _type))
