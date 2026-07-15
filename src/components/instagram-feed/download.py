#!/usr/bin/env python3
"""Wrapper de download do componente: Smash Balloon Social Photo Feed – Easy Social Feeds Plugin."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Smash Balloon Social Photo Feed – Easy Social Feeds Plugin', 'slug': 'instagram-feed', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
