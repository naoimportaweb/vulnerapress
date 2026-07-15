#!/usr/bin/env python3
"""Wrapper de download do componente: Formidable Forms &#8211; WordPress Form Builder for Contact Forms, Calculators, Quizzes &amp; More."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Formidable Forms &#8211; WordPress Form Builder for Contact Forms, Calculators, Quizzes &amp; More', 'slug': 'formidable', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
