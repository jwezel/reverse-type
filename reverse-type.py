#!/bin/env python

from subprocess import run
import sys


def Main():
    """
    Main
    """
    status = run(
        ['xclip', '-in', '-target', 'UTF8_STRING'], input=(chr(0x202E) + ' '.join(sys.argv[1:])[::-1] + chr(0x202C)).encode()
    )
    status.check_returncode()


if __name__ == '__main__':
    Main()
