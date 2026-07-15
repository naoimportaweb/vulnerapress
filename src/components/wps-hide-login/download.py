#!/usr/bin/env python3
"""Wrapper de download do componente: WPS Hide Login."""
import sys
from pathlib import Path

# Coloca src/ no path para importar o módulo compartilhado.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WPS Hide Login', 'slug': 'wps-hide-login', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
