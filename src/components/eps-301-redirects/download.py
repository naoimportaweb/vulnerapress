#!/usr/bin/env python3
"""Wrapper de download do componente: 301 Redirects &#8211; Redirect Manager."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': '301 Redirects &#8211; Redirect Manager', 'slug': 'eps-301-redirects', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
