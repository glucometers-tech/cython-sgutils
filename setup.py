# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: MIT

from setuptools import Extension, find_packages, setup

from Cython.Build import cythonize

with open("README.md", "rt") as fh:
    long_description = fh.read()

setup(
    name="cython-sgutils",
    version="1",
    description="Cython-based bindings for libsgutils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Diego Elio Pettenò",
    author_email="flameeyes@flameeyes.com",
    url="https://github.com/glucometers-tech/cython-sgutils",
    keywords=["scsi"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(),
    ext_modules=cythonize(
        [
            Extension(
                "sgutils.csgutils", ["sgutils/csgutils.pyx"], libraries=["sgutils2"],
            )
        ]
    ),
)
