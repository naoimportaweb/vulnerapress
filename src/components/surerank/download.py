#!/usr/bin/env python3
"""Wrapper de download do componente: SureRank SEO – Smart Assistant with Meta Tags, Social Preview, XML Sitemap, and Schema."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'SureRank SEO – Smart Assistant with Meta Tags, Social Preview, XML Sitemap, and Schema', 'slug': 'surerank', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
