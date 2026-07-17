#!/usr/bin/env python3
"""Wrapper de download do componente: Slider Revolution (RevSlider)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Slider Revolution (RevSlider)', 'slug': 'revslider', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
