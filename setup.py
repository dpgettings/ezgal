#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="EZGal",
    version="1.0.0",
    author="Conor L. Mancone",
    author_email="cmancone@gmail.com",
    description="A Flexible Interface for Stellar Population Synthesis Models",
    long_description=read('README.rst'),
    # license="BSD",
    packages=["ezgal"]
    requires=['numpy', 'pyfits', 'scipy']
    #requires=['numpy', 'pyfits', 'scipy'],
    #install_requires=['numpy','pyfits','scipy']
    # classifiers=[
    #     #"Development Status :: 3 - Alpha",
    #     #"Topic :: Scientific/Engineering :: Visualization",
    #     # "License :: OSI Approved :: BSD License",
    #     ]
)
