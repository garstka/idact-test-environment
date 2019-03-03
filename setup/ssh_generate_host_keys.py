#!/usr/bin/env python3
"""Generates host keys for the ssh daemon in the container."""

import subprocess
import traceback

KEY_TYPES = ['rsa', 'dsa', 'ecdsa']
OPTIONAL_KEY_TYPES = ['ed25519']


def get_command_generate_key(key_type: str):
    generate_key = (r"echo -e 'y\n' |"
                    " ssh-keygen"
                    " -f /etc/ssh/ssh_host_{key_type}_key"
                    " -N ''"
                    " -t {key_type}".format(key_type=key_type))

    return ['bash', '-c', generate_key]


def main():
    """Main script function."""
    for key_type in KEY_TYPES:
        subprocess.check_call(get_command_generate_key(key_type=key_type))
    for key_type in OPTIONAL_KEY_TYPES:
        try:
            subprocess.check_call(get_command_generate_key(key_type=key_type))
        except subprocess.CalledProcessError:
            traceback.print_exc()


if __name__ == '__main__':
    main()
