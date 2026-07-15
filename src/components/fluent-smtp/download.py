#!/usr/bin/env python3
"""Wrapper de download do componente: FluentSMTP &#8211; WP SMTP Plugin with Amazon SES, SendGrid, MailGun, Postmark, Google and Any SMTP Provider."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'FluentSMTP &#8211; WP SMTP Plugin with Amazon SES, SendGrid, MailGun, Postmark, Google and Any SMTP Provider', 'slug': 'fluent-smtp', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
