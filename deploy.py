#!/usr/bin/env python

"""
Script for deploying a new version of the python-asana library.
"""

from __future__ import print_function

import argparse
import re
import subprocess
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'version',
        help='Version to deploy as, in format x.y.z')
    args = parser.parse_args()

    if not re.match('[0-9]+[.][0-9]+[.][0-9]+', args.version):
        print('Invalid version: {}'.format(args.version))
        sys.exit(1)

    with open('asana/version.py', 'w') as version_file:
        version_file.write("VERSION = '{}'\n".format(args.version))

    subprocess.call(
        'git commit -m "Releasing version %s" asana/version.py' % args.version,
        shell=True)
    subprocess.call(
        'git tag %s' % args.version, shell=True)
    subprocess.call(
        'git push --tags origin master:master', shell=True)
    print('Successfully deployed version {}'.format(args.version))
