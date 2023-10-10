#!/usr/bin/env python

import sys
import os
from setuptools import setup, find_packages

assert sys.version_info >= (3, 7), 'We only support Python 3.7+'

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'asana'))

# Safely read the version number from the version.py file
version = {}
with open('asana/version.py') as fp:
    exec(fp.read(), version)

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()

setup(
    name='asana',
    version=version['__version__'],
    description='Asana API client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=[
        'requests >= 2.20.0, == 2.*',
        'requests_oauthlib >= 0.8.0, <2.0',
    ],
    author='Asana, Inc',
    # author_email='',
    url='http://github.com/asana/python-asana',
    packages=find_packages(exclude=('tests', 'examples')),
    keywords='asana',
    zip_safe=True,
    test_suite='tests')
