#!/usr/bin/env python3
import os
import subprocess

WORKING_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '../'))

TAG_NAME_SCRIPT = "dev/tag_name"
TAG_MESSAGE_SCRIPT = "dev/tag_message"


def main():
    """Main script function."""
    os.chdir(WORKING_DIR)
    tag_name = subprocess.check_output([TAG_NAME_SCRIPT]).rstrip()
    tag_message = subprocess.check_output([TAG_MESSAGE_SCRIPT])
    subprocess.check_call(['git', 'tag', '-a', tag_name, '-m', tag_message])


if __name__ == '__main__':
    main()
