#!/usr/bin/env python

import os
import re
import sys
from setuptools import setup, find_packages

from deploy import INIT_FILE, VERSION_REGEX

assert sys.version_info >= (2, 6), 'We only support Python 2.6+'

with open(INIT_FILE) as fobj:
    version = re.search(VERSION_REGEX, fobj.read(), re.MULTILINE).group(2)

if not version:
    raise RuntimeError('Cannot find __version__ in {0}'.format(INIT_FILE))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'asana'))

setup(
    name='asana',
    version=version,
    description='Asana API client',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    install_requires=[
        'requests~=2.9.1',
        'requests_oauthlib~=0.6.1',
        'six~=1.10.0'
    ],
    author='Asana, Inc',
    # author_email='',
    url='http://github.com/asana/python-asana',
    packages=find_packages(exclude=('tests',)),
    keywords='asana',
    zip_safe=True,
    test_suite='tests')
