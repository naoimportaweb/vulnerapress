#!/usr/bin/env python3
"""Wrapper de download do componente: WP Go Maps &#8211; Google Map, OpenStreetMap, Leaflet Map."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WP Go Maps &#8211; Google Map, OpenStreetMap, Leaflet Map', 'slug': 'wp-google-maps', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
