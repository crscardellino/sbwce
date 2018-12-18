#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import fnmatch
import os
import re
import sys
import spacy

from tqdm import tqdm

spacy.prefer_gpu()
nlp = spacy.load("es", disable=['parser', 'ner'])

def traverse_directory(path, file_pattern='*'):
    for root, _, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, file_pattern):
            yield os.path.join(root, filename)


os.makedirs("./parsed_corpora", exist_ok=True)
for dirname in tqdm(sorted(os.listdir("./corpora"))):
    with open("./parsed_corpora/%s.tsv" % dirname, "w") as fho,\
            open("./corpora/%s.txt" % (dirname, dirname), "r") as fhi:
        for line in fhi:
            for token in nlp(line.strip()):
                print(token.i, token.text, token.lemma_, token.pos_,
                      'WSP' if re.match(r'\s+', token.whitespace_) else 'BLK',
                      sep="\t", file=fho)
            print(file=fho)
