#!/usr/bin/env python3
"""Wrapper de download do componente: WP-Optimize – Cache, Compress images, Minify &amp; Clean database to boost page speed &amp; performance."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WP-Optimize – Cache, Compress images, Minify &amp; Clean database to boost page speed &amp; performance', 'slug': 'wp-optimize', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
