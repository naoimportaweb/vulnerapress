#!/usr/bin/env python3
"""Wrapper de download do componente: Custom Fonts &#8211; Host Your Fonts Locally."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Custom Fonts &#8211; Host Your Fonts Locally', 'slug': 'custom-fonts', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
