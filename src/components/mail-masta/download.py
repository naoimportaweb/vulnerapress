#!/usr/bin/env python3
"""Wrapper de download do componente: Mail Masta."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Mail Masta', 'slug': 'mail-masta', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
