#!/usr/bin/env python3
"""Wrapper de download do componente: WPForms &#8211; AI Form Builder for WordPress &#8211; Contact Forms, Payment Forms, Survey Form, Quiz &amp; More."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WPForms &#8211; AI Form Builder for WordPress &#8211; Contact Forms, Payment Forms, Survey Form, Quiz &amp; More', 'slug': 'wpforms-lite', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
