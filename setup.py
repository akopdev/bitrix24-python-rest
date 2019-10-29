#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   ____  _ _        _      ____  _  _     ____  _____ ____ _____
#  | __ )(_) |_ _ __(_)_  _|___ \| || |   |  _ \| ____/ ___|_   _|
#  |  _ \| | __| '__| \ \/ / __) | || |_  | |_) |  _| \___ \ | |
#  | |_) | | |_| |  | |>  < / __/|__   _| |  _ <| |___ ___) || |
#  |____/|_|\__|_|  |_/_/\_\_____|  |_|   |_| \_\_____|____/ |_|

"""
Setup file for Bitrix24 REST API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright (c) 2019 by Akop Kesheshyan.
"""

from distutils.core import setup
from setuptools import find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bitrix24-rest',
    version='1.1.1',
    install_requires=['requests'],
    packages=find_packages(),
    url='https://github.com/akopkesheshyan/bitrix24-python-rest',
    license='MIT',
    author='Akop Kesheshyan',
    author_email='akop.kesheshyan@icloud.com',
    description='Bitrix24 REST API wrapper provides easy way to communicate with bitrix24 portal over REST without OAuth',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='bitrix24 api rest',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
