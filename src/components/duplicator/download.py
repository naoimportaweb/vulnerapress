#!/usr/bin/env python3
"""Wrapper de download do componente: Duplicator &#8211; Backups &amp; Migration Plugin &#8211; Cloud Backups, Scheduled Backups, &amp; More."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Duplicator &#8211; Backups &amp; Migration Plugin &#8211; Cloud Backups, Scheduled Backups, &amp; More', 'slug': 'duplicator', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
