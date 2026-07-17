#!/usr/bin/env python3
"""Sincroniza TODOS os componentes do data/components.json com o cofre.

Lê a lista canônica, deriva o slug (igual ao usado nos subdiretórios) e chama
o módulo compartilhado para cada componente.

Uso:
    python src/sync_all.py            # todos
    python src/sync_all.py yoast-seo  # só os slugs passados
"""
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from downloader import load_env, sync_component

REPO_ROOT = Path(__file__).resolve().parents[1]
COMPONENTS_JSON = REPO_ROOT / "data" / "components.json"


def slug(name: str) -> str:
    s = re.sub(r"[()]", "", name.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def all_components() -> list[dict]:
    data = json.loads(COMPONENTS_JSON.read_text("utf-8"))
    out = []
    for key, kind in (("plugins", "plugin"), ("themes", "theme")):
        for c in data.get(key, []):
            out.append({
                "name": c["name"],
                "slug": c.get("slug") or slug(c["name"]),  # usa slug canônico se houver
                "type": kind,
            })
    return out


def main(argv: list[str]) -> int:
    load_env()
    sleep_seconds = float(os.environ.get("SYNC_SLEEP_SECONDS", "0"))
    wanted = set(argv[1:])
    rc = 0
    first = True
    for comp in all_components():
        if wanted and comp["slug"] not in wanted:
            continue
        if not first and sleep_seconds > 0:
            time.sleep(sleep_seconds)
        first = False
        try:
            rc |= sync_component(**comp)
        except Exception as exc:  # não deixa um componente derrubar o lote
            print(f"[x] {comp['name']}: erro — {exc}", file=sys.stderr)
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
