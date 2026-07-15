#!/usr/bin/env python3
"""Wrapper de download do componente: All-In-One Security (AIOS) – Security and Firewall."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'All-In-One Security (AIOS) – Security and Firewall', 'slug': 'all-in-one-wp-security-and-firewall', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
