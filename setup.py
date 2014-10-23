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
    packages=["ezgal"],
    requires=['numpy', 'pyfits', 'scipy'],
    package_data={
        '': ['*.fits',
             '*README*',
             'data/models/*.model',
             'data/filters/*',
             'data/refs/*',
             'scripts/*']},

    # license="BSD",
    # include_package_data = True
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Astronomy",
        #"License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2 :: Only"
        ]
)
