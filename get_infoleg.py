#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import os
import requests
import sys
import tarfile

from lxml import etree
from tqdm import tqdm

INFOLEG_URL = 'https://cs.famaf.unc.edu.ar/~ccardellino/resources/mirel/law_text_cleaned.tar.bz2'
INFOLEG_TMP = '/tmp/infoleg.tar.bz2'
INFOLEG_OUT = '/tmp/law_text_cleaned/'
INFOLEG_FIL = './corpora/infoleg/infoleg.txt'

os.makedirs(os.path.dirname(INFOLEG_FIL), exist_ok=True)

print("Downloading file...", file=sys.stderr)
req = requests.get(INFOLEG_URL)

with open(INFOLEG_TMP, 'wb') as fh:
    fh.write(req.content)

with tarfile.open(INFOLEG_TMP, 'r') as fi, open(INFOLEG_FIL, 'w') as fo:
    print("Extracting file...", file=sys.stderr)
    fi.extractall(path="/tmp")

    print("Parsing files...", file=sys.stderr)
    for fname in tqdm(os.listdir(INFOLEG_OUT)):
        root = etree.parse(INFOLEG_OUT + fname).getroot()
        print(root.find('text').text, file=fo)
