#!/usr/bin/env python3
"""Wrapper de download do componente: Templately – Elementor &amp; Gutenberg Template Library: 6500+ Free &amp; Pro Ready Templates And Cloud!."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Templately – Elementor &amp; Gutenberg Template Library: 6500+ Free &amp; Pro Ready Templates And Cloud!', 'slug': 'templately', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
