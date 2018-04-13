#!/usr/bin/env python

import sys
import os
from setuptools import setup, find_packages

assert sys.version_info >= (2, 7), 'We only support Python 2.7+'

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'asana'))

setup(
    name='asana',
    version='0.7.0',
    description='Asana API client',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'requests >= 2.14, == 2.*',
        'requests_oauthlib >= 0.8.0, == 0.8.*',
        'six >= 1.10, == 1.*'
    ],
    author='Asana, Inc',
    # author_email='',
    url='http://github.com/asana/python-asana',
    packages=find_packages(exclude=('tests',)),
    keywords='asana',
    zip_safe=True,
    test_suite='tests')
