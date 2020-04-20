# SPDX-FileCopyrightText: 2020 The cython-sgutils Authors
#
# SPDX-License-Identifier: MIT

from setuptools import Extension, find_packages, setup

# Ensure it's present.
import setuptools_scm  # noqa: F401
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
    extras_require={"dev": ["mypy", "pre-commit", "Cython", "setuptools_scm"]},
)
