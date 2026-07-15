#!/usr/bin/env python3
"""Wrapper de download do componente: LightStart &#8211; Maintenance Mode, Coming Soon and Landing Page Builder."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'LightStart &#8211; Maintenance Mode, Coming Soon and Landing Page Builder', 'slug': 'wp-maintenance-mode', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
