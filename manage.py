#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Fallback to Python's unittest when Django isn't available
        import unittest
        base_dir = os.path.dirname(os.path.abspath(__file__))
        tests = unittest.defaultTestLoader.discover(os.path.join(base_dir, 'todoapp'))
        runner = unittest.TextTestRunner()
        result = runner.run(tests)
        sys.exit(not result.wasSuccessful())
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
