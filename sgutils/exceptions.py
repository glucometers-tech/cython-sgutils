# SPDX-FileCopyrightText: 2020 The cython-sgutils Authors
#
# SPDX-License-Identifier: MIT


class IllegalOperation(Exception):
    """Illegal operation (e.g. not supported.)"""


class IllegalRequest(ValueError):
    """Illegal request (e.g. wrong parameters.)"""


class AbortedCommand(Exception):
    """Command aborted by target."""


class UnknownError(Exception):
    """Other remaining errors."""
