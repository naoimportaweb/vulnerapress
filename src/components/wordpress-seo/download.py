#!/usr/bin/env python3
"""Wrapper de download do componente: Yoast SEO &#8211; Advanced SEO with real-time guidance and built-in AI."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Yoast SEO &#8211; Advanced SEO with real-time guidance and built-in AI', 'slug': 'wordpress-seo', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
