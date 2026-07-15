#!/usr/bin/env python3
"""Wrapper de download do componente: TablePress &#8211; Tables in WordPress made easy."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'TablePress &#8211; Tables in WordPress made easy', 'slug': 'tablepress', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
