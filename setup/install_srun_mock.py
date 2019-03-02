#!/usr/bin/env python3
"""Installs `srun` mock. See :mod:`.srun_mock`.

"""

import subprocess

INSTALL_DOS2UNIX = ['yum', '-y', 'install', 'dos2unix']

SET_PERMISSIONS = ['chmod', 'u=rwx,go=rx', '/usr/local/bin/srun']

RUN_DOS2UNIX = ['dos2unix', '/usr/local/bin/srun']


def main():
    print("Installing dos2unix...")
    subprocess.check_call(INSTALL_DOS2UNIX)
    print("Installing srun mock...")
    subprocess.check_call(SET_PERMISSIONS)
    subprocess.check_call(RUN_DOS2UNIX)


if __name__ == '__main__':
    main()
