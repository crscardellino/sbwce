#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import argparse
import logging
import os
import sys
from gensim.models import FastText

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class SentencesIterator(object):
    def __iter__(self):
        for l in sys.stdin:
            yield l.strip().split()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FastText algorithm")
    parser.add_argument("output",
                        type=str,
                        metavar="OUTPUT",
                        help="File to store the word vectors.")
    parser.add_argument("--size",
                        type=int,
                        metavar="SIZE",
                        help="Set size of word vectors.",
                        default=300)
    parser.add_argument("--window",
                        type=int,
                        metavar="WINDOW",
                        help="Max skip length between words.",
                        default=5)
    parser.add_argument("--threads",
                        type=int,
                        metavar="THREADS",
                        help="Set the number of threads for parallelizing.",
                        default=12)
    parser.add_argument("--min_count",
                        type=int,
                        metavar="MIN_COUNT",
                        help="Set the minimum number of occurrences for a word",
                        default=5)
    parser.add_argument("--sample",
                        type=float,
                        metavar="SAMPLE",
                        help="Threshold for configuring which higher-frequency words are randomly downsampled",
                        default=0.001)
    parser.add_argument("--alpha",
                        type=float,
                        metavar="ALPHA",
                        help="Set the starting learning rate",
                        default=0.001)
    parser.add_argument("--iter",
                        type=int,
                        metavar="ITERATIONS",
                        help="number of iterations (epochs) over the corpus.",
                        default=5)
    parser.add_argument("--cbow",
                        action="store_true",
                        help="Train usining CBOW instead of SkipGram.")
    parser.add_argument("--cbow-mean",
                        action="store_true",
                        help="Use mean instead of sum when using CBOW.")
    parser.add_argument("--negs",
                        type=int,
                        metavar="NEGATIVE_SAMPLING_COUNT",
                        help="If > 0, negative sampling will be used, the int for negative specifies how many " +
                             "\"noise words\" should be drawn (usually between 5-20).",
                        default=10)
    args = parser.parse_args()

    model_config = {
        "size": args.size,
        "window": args.window,
        "workers": args.threads,
        "min_count": args.min_count,
        "sample": args.sample,
        "alpha": args.alpha,
        "iter": args.iter,
        "negative": args.negs,
        "sg": 0 if args.cbow else 1,
        "hs": 0 if args.negs > 0 else 1,
        "cbow_mean": 1 if args.cbow_mean else 0
    }

    sentences = SentencesIterator()
 
    print("Creating and Training FastText model.", file=sys.stderr)
    model = FastText(sentences, **model_config)

    print("Saving the FastText model.", file=sys.stderr)
    model.save(args.output)
