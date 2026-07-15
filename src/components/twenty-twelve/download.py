#!/usr/bin/env python3
"""Wrapper de download do componente: Twenty Twelve."""
import sys
from pathlib import Path

# Coloca src/ no path para importar o módulo compartilhado.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Twenty Twelve', 'slug': 'twenty-twelve', 'type': 'theme'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
