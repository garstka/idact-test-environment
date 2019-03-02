#!/usr/bin/env python
"""Installs Python $CONTAINER_PYTHON_VERSION"""

import os
import subprocess


def get_commands_install_python():
    yum_rpm = (
        "https://centos{}.iuscommunity.org/"
        "ius-release.rpm").format(os.environ['CONTAINER_CENTOS_VERSION'])

    install_rpm = ['yum', '-y', 'install', yum_rpm]

    python_package = "python{}u".format(
        os.environ['CONTAINER_PYTHON_VERSION'].replace('.', ''))

    install_packages = ['yum', '-y', 'install',
                        'sqlite-devel',
                        python_package,
                        "{}-pip".format(python_package),
                        "{}-devel".format(python_package)]

    return [install_rpm,
            install_packages]


def main():
    print("Installing Python {CONTAINER_PYTHON_VERSION}...".format(
        CONTAINER_PYTHON_VERSION=os.environ['CONTAINER_PYTHON_VERSION']))

    for i in get_commands_install_python():
        subprocess.check_call(i)


if __name__ == '__main__':
    main()
