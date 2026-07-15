#!/usr/bin/env python3
"""Wrapper de download do componente: SEOPress &#8211; AI SEO Plugin &amp; On-site SEO."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'SEOPress &#8211; AI SEO Plugin &amp; On-site SEO', 'slug': 'wp-seopress', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
