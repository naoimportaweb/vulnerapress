#!/usr/bin/env python3
"""Wrapper de download do componente: Category Order and Taxonomy Terms Order."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Category Order and Taxonomy Terms Order', 'slug': 'taxonomy-terms-order', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
