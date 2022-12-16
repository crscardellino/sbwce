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
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(fi, path="/tmp")

    print("Parsing files...", file=sys.stderr)
    for fname in tqdm(os.listdir(INFOLEG_OUT)):
        root = etree.parse(INFOLEG_OUT + fname).getroot()
        print(root.find('text').text, file=fo)
