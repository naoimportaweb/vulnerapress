#!/usr/bin/env python3
"""Wrapper de download do componente: WP Statistics – Simple, privacy-friendly Google Analytics alternative."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WP Statistics – Simple, privacy-friendly Google Analytics alternative', 'slug': 'wp-statistics', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
