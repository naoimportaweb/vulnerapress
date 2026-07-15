#!/usr/bin/env python3
"""Wrapper de download do componente: Kirki – Freeform Page Builder, Website Builder &amp; Customizer."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Kirki – Freeform Page Builder, Website Builder &amp; Customizer', 'slug': 'kirki', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
