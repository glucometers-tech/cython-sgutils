# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: MIT

from setuptools import Extension, find_packages, setup

import setuptools_scm  # Ensure it's present.
from Cython.Build import cythonize

setup(
    packages=find_packages(),
    package_data={"": ["*.pyx", "*.pxd"]},
    ext_modules=cythonize(
        [
            Extension(
                "sgutils.csgutils", ["sgutils/csgutils.pyx"], libraries=["sgutils2"],
            )
        ]
    ),
    extras_require={"dev": ["mypy", "pre-commit", "Cython", "setuptools_scm"],},
)
