#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'selenium',
    'django',
    'BeautifulSoup4',
    'requests',
]

test_requirements = [
    # TODO: put package test requirements here
    'selenium',
    'django',
    'BeautifulSoup4',
    'requests',
]

setup(
    name='acascraper',
    version='0.1.0',
    description='Academic social network scraper package',
    long_description=readme + '\n\n' + history,
    author='Andrew Stretton',
    author_email='andrew.stretton@sgc.ox.ac.uk',
    url='https://github.com/strets123/acascraper',
    packages=[
        'acascraper',
    ],
    package_dir={'acascraper':
                 'acascraper'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='acascraper',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)