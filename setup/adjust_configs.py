#!/usr/bin/env python3
"""Adjusts the Slurm and supervisord configs."""

import subprocess

ADD_MEMORY_COMMAND = ['sed',
                      '-i',
                      "s/RealMemory=1000/RealMemory=2000/g;"
                      " s/MaxNodes=1/MaxNodes=2/g;"
                      " s/PartitionName=normal Nodes=c"
                      "/PartitionName=debug Nodes=c/g",
                      "/etc/slurm/slurm.conf"]

AUTORESTART_COMMAND = ['sed',
                       '-i',
                       "s/autorestart=false/autorestart=true/g",
                       "/etc/supervisord.conf"]


def main():
    subprocess.check_call(ADD_MEMORY_COMMAND)
    subprocess.check_call(AUTORESTART_COMMAND)


if __name__ == '__main__':
    main()
