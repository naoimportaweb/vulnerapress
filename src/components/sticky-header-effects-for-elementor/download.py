#!/usr/bin/env python3
"""Wrapper de download do componente: Sticky Header Effects for Elementor."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Sticky Header Effects for Elementor', 'slug': 'sticky-header-effects-for-elementor', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
