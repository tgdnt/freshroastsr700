# -*- coding: utf-8 -*-
# Copyright (c) 2015-2016 Mark Spicer
# Made available under the MIT license.

import os
from setuptools import setup
from setuptools import find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.org')) as f:
    long_description = f.read()

# import version number
version = {}
with open("./freshroastsr700/version.py") as fp:
    exec(fp.read(), version)
# later on we use: version['__version__']

setup(
    name='freshroastsr700',
    version=version['__version__'],
    description='A modified version of FreshRoastSR700 that cycles heat setting \'cool\' instead of \'low\' to regulate temperature.',
    long_description=long_description,
    url='https://github.com/tgdnt/freshroastsr700',
    author='Mark Spicer, Caleb Coffee, Tom Rankin',
    author_email='mds4680@rit.edu',
    maintainer='Tiago Donato',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pyserial>=3.0.1'
    ]
)
