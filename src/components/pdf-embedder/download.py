#!/usr/bin/env python3
"""Wrapper de download do componente: PDF Embedder."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'PDF Embedder', 'slug': 'pdf-embedder', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
