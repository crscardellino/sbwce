#!/usr/bin/env bash

>&2 echo "Getting wikiextractor"
curl -fsSL https://raw.githubusercontent.com/attardi/wikiextractor/master/WikiExtractor.py -o /tmp/wikiextractor.py

mkdir -p logs

for file in wikibooks wikinews wikipedia wikiquote wikisource wikiversity wikivoyage
do
    >&2 echo "Extracting $file"
    python /tmp/wikiextractor.py -o - \
        --list --filter_disambig_pages \
        ./corpora/$file/$file.xml 2> ./logs/$file.log | sed 's/^-\s*//' > ./corpora/$file/$file.txt
done

>&2 echo "All files extracted"
