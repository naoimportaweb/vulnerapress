#!/usr/bin/env python3
"""Wrapper de download do componente: Popup Maker &#8211; Boost Sales, Conversions, Optins, Subscribers with the Ultimate WP Popup Builder."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Popup Maker &#8211; Boost Sales, Conversions, Optins, Subscribers with the Ultimate WP Popup Builder', 'slug': 'popup-maker', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
