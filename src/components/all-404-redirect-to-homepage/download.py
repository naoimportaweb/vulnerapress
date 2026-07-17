#!/usr/bin/env python3
"""Wrapper de download do componente: All 404 Redirect to Homepage."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'All 404 Redirect to Homepage', 'slug': 'all-404-redirect-to-homepage', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
