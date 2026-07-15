#!/usr/bin/env python3
"""Wrapper de download do componente: Elementor Website Builder &#8211; more than just a page builder."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Elementor Website Builder &#8211; more than just a page builder', 'slug': 'elementor', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
