#!/usr/bin/env python3
"""Wrapper de download do componente: Web Accessibility (formally known as Ally) &#8211; WCAG Scanning, Guided Fixes, Usability Widget."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Web Accessibility (formally known as Ally) &#8211; WCAG Scanning, Guided Fixes, Usability Widget', 'slug': 'pojo-accessibility', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
