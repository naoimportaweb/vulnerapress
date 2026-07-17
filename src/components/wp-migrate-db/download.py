#!/usr/bin/env python3
"""Wrapper de download do componente: WP Migrate Lite &#8211; Migration Made Easy."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WP Migrate Lite &#8211; Migration Made Easy', 'slug': 'wp-migrate-db', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
