#!/usr/bin/env python

"""
Script for deploying a new version of the python-asana library.
"""

from __future__ import print_function

import argparse
import subprocess

if __name__ == '__main__':
    # Setup parser for command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'part',
        choices=['major', 'minor', 'patch'],
        help='The part of the version to be bumped'
    )
    args = parser.parse_args()

    # Get the current version from asana/version.py
    current_version = {}
    with open('asana/version.py') as fp:
        exec(fp.read(), current_version)
    major, minor, patch = current_version['__version__'].split('.')

    # Bump version part based on argument provided
    if args.part == 'major':
        major = str(int(major) + 1)
    if args.part == 'minor':
        minor = str(int(minor) + 1)
    if args.part == 'patch':
        patch = str(int(patch) + 1)

    # Overwrite the version in VERSION and asana/version.py
    updated_version = "{}.{}.{}".format(major, minor, patch)
    with open('VERSION', 'w') as version_file:
        version_file.write("{}".format(updated_version))
    with open('asana/version.py', 'w') as version_file:
        version_file.write("__version__ = '{}'\n".format(updated_version))

    # Add, commit and push version changes to GitHub and tag release
    subprocess.call('git add VERSION asana/version.py', shell=True)
    subprocess.call(
        'git commit -m "Releasing version {}"'.format(updated_version), shell=True
    )
    subprocess.call('git tag v{}'.format(updated_version), shell=True)
    subprocess.call('git push --tags origin master:master', shell=True)

    print('Successfully deployed version {}'.format(updated_version))
