#!/usr/bin/env python3
"""Wrapper de download do componente: Kadence Blocks — Page Builder Toolkit for Gutenberg Editor."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Kadence Blocks — Page Builder Toolkit for Gutenberg Editor', 'slug': 'kadence-blocks', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
