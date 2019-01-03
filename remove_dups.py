#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import sys

from hashlib import md5


hashes = set()
for line in sys.stdin:
    line_hash = md5(line.strip().encode("utf-8")).hextdigest()
    if line_hash not in hashes:
        print(line_hash)
        hashes.add(line_hash)

