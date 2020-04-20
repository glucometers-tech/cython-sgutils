# SPDX-FileCopyrightText: 2020 The cython-sgutils Authors
#
# SPDX-License-Identifier: MIT

import dataclasses


@dataclasses.dataclass
class SimpleInquiryResp:
    """Information as returned by the simple_inquiry() function."""

    peripheral_qualified: int
    peripheral_type: int
    byte_1: int

    version: int
    byte_3: int
    byte_5: int
    byte_6: int
    byte_7: int

    vendor: bytes
    product: bytes
    revision: bytes
