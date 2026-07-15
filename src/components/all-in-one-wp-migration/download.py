#!/usr/bin/env python3
"""Wrapper de download do componente: All-in-One WP Migration and Backup."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'All-in-One WP Migration and Backup', 'slug': 'all-in-one-wp-migration', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
