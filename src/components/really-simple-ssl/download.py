#!/usr/bin/env python3
"""Wrapper de download do componente: Really Simple Security &#8211; Simple and Performant Security (formerly Really Simple SSL)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Really Simple Security &#8211; Simple and Performant Security (formerly Really Simple SSL)', 'slug': 'really-simple-ssl', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
