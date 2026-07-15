#!/usr/bin/env python3
"""Wrapper de download do componente: Rank Math SEO – AI SEO Tools to Dominate SEO Rankings."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Rank Math SEO – AI SEO Tools to Dominate SEO Rankings', 'slug': 'seo-by-rank-math', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
