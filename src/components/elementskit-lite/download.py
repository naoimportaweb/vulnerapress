#!/usr/bin/env python3
"""Wrapper de download do componente: ElementsKit Elementor Addons – Advanced Widgets &amp; Templates Addons for Elementor."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'ElementsKit Elementor Addons – Advanced Widgets &amp; Templates Addons for Elementor', 'slug': 'elementskit-lite', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
