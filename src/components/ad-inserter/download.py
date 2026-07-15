#!/usr/bin/env python3
"""Wrapper de download do componente: Ad Inserter &#8211; Ad Manager &amp; AdSense Ads."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Ad Inserter &#8211; Ad Manager &amp; AdSense Ads', 'slug': 'ad-inserter', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
