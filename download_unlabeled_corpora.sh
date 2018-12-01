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
        wget -O $dirname.xml.bz2 $link
        bunzip2 $dirname.xml.bz2
    elif [[ $link =~ \.*\.tar\.gz$ ]]
    then
        wget -O $dirname.tar.gz $link
        tar xvf $dirname.tar.gz
        find . -type f -name "*xml.gz" -exec gunzip {} \+
        find . -type f -name "*html.gz" -exec gunzip {} \+  # for PHP
    else
        wget -O $dirname.txt.gz $link
        gunzip $dirname.txt.gz
    fi
    cd ../..
done

>&2 echo "All links fetched"
