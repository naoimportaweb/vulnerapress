#!/usr/bin/env python3
"""Wrapper de download do componente: Jetpack &#8211; WP Security, Backup, Speed, &amp; Growth."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Jetpack &#8211; WP Security, Backup, Speed, &amp; Growth', 'slug': 'jetpack', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
