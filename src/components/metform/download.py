#!/usr/bin/env python3
"""Wrapper de download do componente: MetForm &#8211; Contact Form, Survey, Quiz, &amp; Custom Form Builder for Elementor."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'MetForm &#8211; Contact Form, Survey, Quiz, &amp; Custom Form Builder for Elementor', 'slug': 'metform', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
