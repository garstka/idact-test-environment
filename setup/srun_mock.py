#!/usr/bin/env python
"""Slurm installation in the container does not support job steps.
    This is why `srun` should be mostly a passthrough, and provide any
    expected side-effects for tests.

"""

import subprocess
import sys


def main(argv):
    command_start = 1
    return subprocess.call(argv[command_start:])


if __name__ == '__main__':
    sys.exit(main(sys.argv))
