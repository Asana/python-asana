#!/usr/bin/env python

"""
Script for deploying a new version of the python-asana library.
"""

import argparse
import re
import subprocess

VERSION_REGEX = r'^(__version__\s*=\s*[\'"])([^\'"]*)([\'"])'
INIT_FILE = 'asana/__init__.py'


def deploy():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'version',
        help='Version to deploy as, in format x.y.z')
    args = parser.parse_args()

    if not re.match('[0-9]+[.][0-9]+[.][0-9]+', args.version):
        argparse.error('Invalid version: {0}'.format(args.version))

    with open(INIT_FILE) as init_file:
        init_file_contents = init_file.read()

    repl = r'\g<1>{0}\g<3>'.format(args.version)
    new_file_contents = re.sub(
        VERSION_REGEX, repl, init_file_contents, flags=re.MULTILINE)

    with open(INIT_FILE, 'w') as init_file:
        init_file.write(new_file_contents)

    subprocess.call(
        'git commit -m "Releasing version %s" asana/version.py' % args.version,
        shell=True)
    subprocess.call(
        'git tag %s' % args.version, shell=True)
    subprocess.call(
        'git push --tags origin master:master', shell=True)
    print 'Successfully deployed version %s' % args.version


if __name__ == '__main__':
    deploy()
