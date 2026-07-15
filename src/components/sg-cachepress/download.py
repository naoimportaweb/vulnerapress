#!/usr/bin/env python3
"""Wrapper de download do componente: Speed Optimizer &#8211; The All-In-One Performance-Boosting Plugin."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Speed Optimizer &#8211; The All-In-One Performance-Boosting Plugin', 'slug': 'sg-cachepress', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
