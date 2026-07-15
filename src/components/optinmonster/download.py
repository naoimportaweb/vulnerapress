#!/usr/bin/env python3
"""Wrapper de download do componente: Popup Builder &amp; Popup Maker for WordPress – OptinMonster Email Marketing and Lead Generation."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Popup Builder &amp; Popup Maker for WordPress – OptinMonster Email Marketing and Lead Generation', 'slug': 'optinmonster', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
