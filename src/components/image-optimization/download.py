#!/usr/bin/env python3
"""Wrapper de download do componente: Image Optimization &#8211; Compress Images and Convert to WebP or AVIF."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Image Optimization &#8211; Compress Images and Convert to WebP or AVIF', 'slug': 'image-optimization', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
