#!/usr/bin/env python3
"""Installs Jupyter Notebook, Jupyter Hub and Jupyter Lab."""

import os
import subprocess


def get_python():
    return "python{CONTAINER_PYTHON_VERSION}".format(
        CONTAINER_PYTHON_VERSION=os.environ['CONTAINER_PYTHON_VERSION'])


def get_command_install_jupyter():
    return [get_python(), '-m', 'pip', 'install', 'jupyter']


def get_commands_install_jupyter_hub():
    install_npm = ['yum', '-y', 'install', 'npm']
    disable_strict_ssl = ['npm', 'config', 'set', 'strict-ssl', 'false']
    install_proxy = ['npm', 'install', '-y', '-g', 'configurable-http-proxy']
    install_jupyter_hub = [get_python(), '-m', 'pip', 'install', 'jupyterhub']

    return [install_npm,
            disable_strict_ssl,
            install_proxy,
            install_jupyter_hub]


def get_command_install_jupyter_lab():
    return [get_python(), '-m', 'pip', 'install', 'jupyterlab']


def main():
    print("Installing Jupyter...")
    subprocess.check_call(get_command_install_jupyter())

    print("Installing Jupyter Hub...")
    for i in get_commands_install_jupyter_hub():
        subprocess.check_call(i)

    print("Installing Jupyter Lab...")
    subprocess.check_call(get_command_install_jupyter_lab())


if __name__ == '__main__':
    main()
