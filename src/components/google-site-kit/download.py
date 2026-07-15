#!/usr/bin/env python3
"""Wrapper de download do componente: Site Kit by Google &#8211; Analytics, Search Console, AdSense, Speed."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Site Kit by Google &#8211; Analytics, Search Console, AdSense, Speed', 'slug': 'google-site-kit', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
