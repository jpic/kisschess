#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='kisschess',
    version="0.0",
    author='James Pic',
    author_email='jpic@yourlabs.org',
    description='Chess client that uses your console and browser',
    url='http://github.com/jpic/kisschess',
    packages=find_packages(),
    include_package_data=True,
)
