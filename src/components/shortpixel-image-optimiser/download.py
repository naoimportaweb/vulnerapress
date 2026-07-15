#!/usr/bin/env python3
"""Wrapper de download do componente: ShortPixel Image Optimizer &#8211; Optimize Images, Convert WebP &amp; AVIF."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'ShortPixel Image Optimizer &#8211; Optimize Images, Convert WebP &amp; AVIF', 'slug': 'shortpixel-image-optimiser', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
