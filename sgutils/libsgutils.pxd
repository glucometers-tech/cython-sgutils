# cython: language_level=3

# SPDX-FileCopyrightText: 2004-2019 Douglas Gilbert.
# SPDX-FileCopyrightText: 2020 The cython-sgutils Authors
#
# SPDX-License-Identifier: MIT

from libc.stdint cimport *

cdef extern from "scsi/sg_lib.h":
    cdef enum:
        SG_LIB_CAT_CLEAN
        SG_LIB_CAT_INVALID_OP
        SG_LIB_CAT_ILLEGAL_REQ
        SG_LIB_CAT_ABORTED_COMMAND

cdef extern from "scsi/sg_cmds_basic.h":
    cdef struct sg_simple_inquiry_resp:
        uint8_t peripheral_qualifier
        uint8_t peripheral_type
        uint8_t byte_1

        uint8_t version
        uint8_t byte_3
        uint8_t byte_5
        uint8_t byte_6
        uint8_t byte_7
        char[9] vendor
        char[17] product
        char[5] revision

    int sg_simple_inquiry(int sg_fd, sg_simple_inquiry_resp *inq_data,
                          bint noisy, int verbose)
