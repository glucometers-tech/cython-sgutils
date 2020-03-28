# Copyright (c) 2020 The cython-sgutils authors.
# SPDX-License-Identifier: MIT
# cython: language_level=3

from sgutils cimport libsgutils
from sgutils import exceptions, structs


def simple_inquiry(fid, bint noisy=False, int verbose=0):
    cdef libsgutils.sg_simple_inquiry_resp resp
    result = libsgutils.sg_simple_inquiry(
        fid.fileno(),
        &resp,
        noisy,
        verbose,
    )
    if result == libsgutils.SG_LIB_CAT_CLEAN:
        return structs.SimpleInquiryResp(
            resp.peripheral_qualifier,
            resp.peripheral_type,
            resp.byte_1,
            resp.version,
            resp.byte_3,
            resp.byte_5,
            resp.byte_6,
            resp.byte_7,
            resp.vendor,
            resp.product,
            resp.revision)
    elif result == libsgutils.SG_LIB_CAT_INVALID_OP:
        raise exceptions.InvalidOperation("Not supported")
    elif result == libsgutils.SG_LIB_CAT_ILLEGAL_REQ:
        raise exceptions.IllegalRequest("Bad field in cdb")
    elif result == libsgutils.SG_LIB_CAT_ABORTED_COMMAND:
        raise exceptions.AbortedCommand()
    elif result < 0:
        raise OSError(-result)
    else:
        raise exceptions.UnknownError("Unknown error %d" % result)
