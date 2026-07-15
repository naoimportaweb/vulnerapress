#!/usr/bin/env python3
"""Wrapper de download do componente: MonsterInsights &#8211; Google Analytics Dashboard for WordPress (Website Stats Made Easy)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'MonsterInsights &#8211; Google Analytics Dashboard for WordPress (Website Stats Made Easy)', 'slug': 'google-analytics-for-wordpress', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
