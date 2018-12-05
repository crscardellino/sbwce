#!/usr/bin/env bash

cat unlabeled_corpora.tsv | while read resource
do
    dirname=$(echo -n $resource | awk '{ print $1 }')
    link=$(echo -n $resource | awk '{ print $3 }')

    >&2 echo "Fetching $link"
    mkdir -p corpora/$dirname
    cd corpora/$dirname
    if [[ $link =~ .*\.xml\.bz2$ ]]
    then
        curl -L -o $dirname.xml.bz2 $link
        bunzip2 $dirname.xml.bz2
    else
        curl -L -o $dirname.txt.gz $link
        gunzip $dirname.txt.gz
    fi
    cd ../..
done

>&2 echo "All links fetched"
