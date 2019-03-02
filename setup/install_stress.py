#!/usr/bin/env python3
"""Installs stress."""

import subprocess

COMMAND_INSTALL_STRESS = ['yum', '-y', 'install', 'stress']


def main():
    print("Installing stress...")
    subprocess.check_call(COMMAND_INSTALL_STRESS)


if __name__ == '__main__':
    main()
