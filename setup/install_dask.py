#!/usr/bin/env python3
"""Installs Dask, Dask Distributed and bokeh."""

import os
import subprocess


def get_command_install_dask():
    python = 'python{CONTAINER_PYTHON_VERSION}'.format(
        CONTAINER_PYTHON_VERSION=os.environ['CONTAINER_PYTHON_VERSION'])

    return [python, '-m', 'pip', 'install', 'dask', 'distributed', 'bokeh']


def main():
    print("Installing Dask, Dask.distributed and bokeh...")
    subprocess.check_call(get_command_install_dask())


if __name__ == '__main__':
    main()
