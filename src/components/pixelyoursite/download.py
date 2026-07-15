#!/usr/bin/env python3
"""Wrapper de download do componente: PixelYourSite &#8211; Your smart PIXEL (TAG) &amp; API Manager."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'PixelYourSite &#8211; Your smart PIXEL (TAG) &amp; API Manager', 'slug': 'pixelyoursite', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
