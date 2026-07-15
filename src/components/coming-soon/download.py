#!/usr/bin/env python3
"""Wrapper de download do componente: Website Builder by SeedProd — Theme Builder, Landing Page Builder, Coming Soon Page, Maintenance Mode."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Website Builder by SeedProd — Theme Builder, Landing Page Builder, Coming Soon Page, Maintenance Mode', 'slug': 'coming-soon', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
