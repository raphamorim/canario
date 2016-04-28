#!/usr/bin/env python

import sys
from setuptools import setup

setup(
    name='capivara',
    version='1.0.2',
    description='Generates & Obtain DOM (Document Object Model)',
    author='Raphael Amorim',
    author_email='rapha850@gmail',
    keywords='dom javascript object model development',
    url='https://github.com/raphamorim/capivara',
    packages=['capivara'],
    install_requires=['nose'],
    include_package_data=True,
    license='Apache 2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)