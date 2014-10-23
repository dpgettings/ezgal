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
    # author_email="",
    description="",
    long_description=read('README.md'),
    # license="BSD",
    packages=["ezgal"]
    requires=['numpy'],  # scipy not required, but strongly recommended
    install_requires=['numpy','pyfits','scipy']
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Visualization",
        # "License :: OSI Approved :: BSD License",
        ]
)
