#!/usr/bin/env python3
"""Wrapper de download do componente: WP Armour &#8211; Honeypot Anti Spam."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WP Armour &#8211; Honeypot Anti Spam', 'slug': 'honeypot', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
