#!/usr/bin/env python3
"""Wrapper de download do componente: TranslatePress &#8211; Translate Multilingual sites with AI Translation."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'TranslatePress &#8211; Translate Multilingual sites with AI Translation', 'slug': 'translatepress-multilingual', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
