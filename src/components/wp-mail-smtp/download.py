#!/usr/bin/env python3
"""Wrapper de download do componente: WP Mail SMTP by WPForms &#8211; The Most Popular SMTP and Email Log Plugin."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WP Mail SMTP by WPForms &#8211; The Most Popular SMTP and Email Log Plugin', 'slug': 'wp-mail-smtp', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
