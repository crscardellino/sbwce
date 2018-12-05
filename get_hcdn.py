#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import bz2
import json
import os
import requests

HCDN_URL = 'https://cs.famaf.unc.edu.ar/~ccardellino/resources/hcdn/hcdn.jsonlines.bz2'
HCDN_TMP = '/tmp/hcdn.jsonlines.bz2'
HCDN_FIL = './corpora/hcdn/hcdn.txt'

os.makedirs(os.path.dirname(HCDN_FIL), exist_ok=True)

req = requests.get(HCDN_URL)

with open(HCDN_TMP, 'wb') as fh:
    fh.write(req.content)

with bz2.open(HCDN_TMP, 'r') as fi, open(HCDN_FIL, 'w') as fo:
    for line in fi:
        line = json.loads(line)
        print(line['summary'].strip(), file=fo)
        print(line['law_text'].strip(), file=fo, end='\n\n')

