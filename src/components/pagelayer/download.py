#!/usr/bin/env python3
"""Wrapper de download do componente: Page Builder: Pagelayer &#8211; Drag and Drop website builder."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Page Builder: Pagelayer &#8211; Drag and Drop website builder', 'slug': 'pagelayer', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
