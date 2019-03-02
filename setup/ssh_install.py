#!/usr/bin/env python3
"""Installs the ssh daemon in the container."""

import subprocess

INSTALL_COMMAND = ['yum', '-y', 'install', 'openssh-server']

SSH_INTERNAL_PORTS = [22, 8022, 8023, 8024, 8025]


def get_append_port_command(port: int):
    return ['sed', '-i', r"$ a\Port {port}".format(port=port),
            '/etc/ssh/sshd_config']


def main():
    """Main script function."""
    subprocess.check_call(INSTALL_COMMAND)
    for port in SSH_INTERNAL_PORTS:
        subprocess.check_call(get_append_port_command(port=port))


if __name__ == '__main__':
    main()
