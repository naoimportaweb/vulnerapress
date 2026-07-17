#!/usr/bin/env python3
"""Wrapper de download do componente: Jetpack Boost &#8211; Website Speed, Performance and Critical CSS."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Jetpack Boost &#8211; Website Speed, Performance and Critical CSS', 'slug': 'jetpack-boost', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
