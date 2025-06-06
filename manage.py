#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        error_msg = (
            'Could not import Django. Are you sure it is installed and '
            'available on your PYTHONPATH environment variable? Did you '
            'forget to activate a virtual environment?'
        )
        raise ImportError(error_msg) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
