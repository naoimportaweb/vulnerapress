#!/usr/bin/env python3
"""Wrapper de download do componente: Essential Addons for Elementor &#8211; Popular Elementor Templates &amp; Widgets."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Essential Addons for Elementor &#8211; Popular Elementor Templates &amp; Widgets', 'slug': 'essential-addons-for-elementor-lite', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
