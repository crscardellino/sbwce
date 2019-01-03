#!/usr/bin/env bash

find ./parsed_corpora -type f -exec cat {} \; | \
    awk '/^\s*$/{ print " " } /^\S*/{ if ($2 ~ /^\w/) { printf("%s ", $2) } }' | \
    awk '{ if (NF >= 5) { print $0 } }' | cat -s 
