#!/usr/bin/env python3
"""Wrapper de download do componente: Social Sharing Plugin &#8211; Social Warfare."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Social Sharing Plugin &#8211; Social Warfare', 'slug': 'social-warfare', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
