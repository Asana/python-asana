#!/usr/bin/env python

"""
Script for deploying a new version of the python-asana library.
"""

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
    print 'Invalid version: %s' % args.version
    sys.exit(1)

  version_file = open('asana/version.py', 'w')
  version_file.write("VERSION = '%s'\n" % args.version)
  version_file.close()

  subprocess.call(
    'git commit -m "Releasing version %s" asana/version.py' % args.version, shell=True)
  subprocess.call(
    'git tag %s' % args.version, shell=True)
  subprocess.call(
    'git push --tags origin master:master', shell=True)
  print 'Successfully deployed version %s' % args.version
