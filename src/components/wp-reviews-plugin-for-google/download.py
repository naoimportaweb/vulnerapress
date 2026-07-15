#!/usr/bin/env python3
"""Wrapper de download do componente: Widgets for Google Reviews."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Widgets for Google Reviews', 'slug': 'wp-reviews-plugin-for-google', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
