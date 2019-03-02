#!/usr/bin/env python3
"""Runs `flake8`."""

import os
import subprocess

import sys

WORKING_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '../'))

FLAKE8_COMMAND = [sys.executable, '-m', 'pytest', '-v', '--flake8', '-m',
                  'flake8']


def main():
    """Main script function."""
    os.chdir(WORKING_DIR)
    subprocess.check_call(FLAKE8_COMMAND)


if __name__ == '__main__':
    main()
