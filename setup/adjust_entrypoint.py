#!/usr/bin/env python3
"""Adds commands that need to be executed after the container starts."""

ENTRYPOINT_FILE = "/usr/local/bin/docker-entrypoint.sh"

UPDATE_HOSTS_COMMAND = ("echo 127.0.0.1 c1 c2 c3 c4 c5 c6 c7 c8 c9 c10"
                        " >> /etc/hosts\n")

RUN_SSHD_COMMAND = "/usr/sbin/sshd\n"

EXEC_LINE = 'exec "$@"\n'


def main():
    with open(ENTRYPOINT_FILE, 'r') as f:
        lines = f.readlines()

    lines = lines[:lines.index(EXEC_LINE)]

    lines.append(UPDATE_HOSTS_COMMAND)
    lines.append(RUN_SSHD_COMMAND)
    lines.append(EXEC_LINE)

    with open(ENTRYPOINT_FILE, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    main()
