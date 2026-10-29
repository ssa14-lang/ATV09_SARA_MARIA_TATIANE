#!/usr/bin/env python
"""Utilitário de linha de comando do Django (runserver, migrate, etc.)."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Você ativou o ambiente virtual "
            "e instalou as dependências (pip install -r requirements.txt)?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
