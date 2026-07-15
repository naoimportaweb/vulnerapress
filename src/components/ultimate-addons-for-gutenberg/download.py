#!/usr/bin/env python3
"""Wrapper de download do componente: Spectra Legacy – Gutenberg Blocks."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Spectra Legacy – Gutenberg Blocks', 'slug': 'ultimate-addons-for-gutenberg', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
