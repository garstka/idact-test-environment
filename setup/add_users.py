#!/usr/bin/env python3
"""Adds $CONTAINER_USERS users to the container:
   (user-0, pass-0), (user-1, pass-1), ...
"""

import os
import subprocess

ADD_USER_COMMAND = "useradd user-{i}"

SET_PASS_COMMAND = r"echo -e 'pass-{i}\npass-{i}' | passwd --stdin user-{i}"


def get_user_count():
    return int(os.environ['CONTAINER_USERS'])


def get_command_add_users():
    add_users = '&&'.join([ADD_USER_COMMAND.format(i=i)
                           for i in range(0, get_user_count())])
    return ['bash', '-c', add_users]


def get_command_set_passwords():
    set_passwords = '&&'.join([SET_PASS_COMMAND.format(i=i)
                               for i in range(0, get_user_count())])
    return ['bash', '-c', set_passwords]


def main():
    print("Adding users...")
    subprocess.check_call(get_command_add_users())
    print("Setting passwords...")
    subprocess.check_call(get_command_set_passwords())


if __name__ == '__main__':
    main()
