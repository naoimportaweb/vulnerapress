#!/usr/bin/env python3
"""Wrapper de download do componente: PrettyLinks – Affiliate Link Management, URL Shortener, Link Cloaking, Tracking &amp; Branded Short Links."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'PrettyLinks – Affiliate Link Management, URL Shortener, Link Cloaking, Tracking &amp; Branded Short Links', 'slug': 'pretty-link', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
