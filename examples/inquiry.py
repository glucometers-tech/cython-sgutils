#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2020 The cython-sgutils Authors
#
# SPDX-License-Identifier: MIT

import argparse

import sgutils


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("device", action="store", help="Path to device to inquiry.")

    args = parser.parse_args()

    with open(args.device, mode="w+b") as device:
        print(sgutils.simple_inquiry(device))


if __name__ == "__main__":
    main()
