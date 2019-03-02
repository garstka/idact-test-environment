#!/usr/bin/env python3
import os
import subprocess

WORKING_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '../'))

BRANCH_NAME_SCRIPT = "dev/branch_name"


def main():
    """Main script function."""
    os.chdir(WORKING_DIR)
    branch_name = subprocess.check_output([BRANCH_NAME_SCRIPT]).rstrip()
    subprocess.check_call(['git', 'checkout', '-b', branch_name])


if __name__ == '__main__':
    main()
