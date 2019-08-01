Spanish Billion Words Corpus and Embeddings
===========================================

Summary
-------

This is the Spanish Billion Words Corpus and Embeddings linguistic resource.

This resource consists of an unannotated corpus of the Spanish language of
more than 2 billion words in 95 million sentences and more than 1.8 million
unique words, compiled from different corpora and resources from the web; and
a set of word embeddings, created from this corpus with
[Word2Vec](https://code.google.com/p/word2vec/) and
[FastText](https://fasttext.cc/), using the
[gensim](https://radimrehurek.com/gensim/) Python library implementation of
these algorithms.

Resources
---------

The corpus can be downloaded in three different formats:

### Raw Corpora

This is the corpus "as is", in a compiled version of all the files downloaded
directly from its respective sources, with almost no preprocessing (except
for the tag removing in the files coming from Wikimedia dumps).

- [Raw Corpora Download](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/sbwce.raw.tar.bz2)

### Tagged Corpora

This is a "tagged" version of the corpus, that has been processed with the
[Spacy](https://spacy.io/) library. The tagged version has one entry per
word, with a blank space dividing the sentences. Each word has the following
information:

    Position Token Lemma Part-of-Speech Whitespace

In this case, the `Position` is an index starting from `0`. The `Token` is
the raw word. The `Lemma` is the lemma of the word as returned by Spacy. The
`Part-of-Speech` is the PoS tag also returned by Spacy. And finally, the
`Whitespace` has two possible values: `WSP` if the token is followed by a
Whitespace, and `BLK` if the token is not followed by a whitespace (e.g. the
token right before a puntuation mark).

- [Tagged Corpora Download](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/sbwce.tagged.tar.bz2)

### Clean Corpora

The "clean" version of this corpus is one single text file with the whole
corpus compiled, where each line represents a sentence from the corpus. Also,
this file was preprocessed to remove all the duplicate sentences from the
corpus. This is the version of the corpus that was used to train the word
embeddings.

- [Clean Corpora Download](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/sbwce.clean.txt.bz2)

### Embeddings

I have trained the embeddings using both Word2Vec and FastText algorithms,
both using the CBOW and the Skipgram models for each of them. Some of the
hyperparameters chosen for the algorithms were:

- Embeddings dimensions: 300
- Window size: 5
- Minimum word frequency: 5
- Number of noise words for negative sampling: 10
- Number of most frequent words downsampled: 27

The rest of the hyperparameters were setup to the default values of the
libraries.

- [Vocabulary Count Download](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vocabulary-min5.txt)

#### Word2Vec Embeddings Downloads

- [Binary CBOW Model](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5-cbow.bin.gz)
- [Text CBOW Model](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5-cbow.txt.bz2)
- [Binary Skipgram Model](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5-skipgram.bin.gz)
- [Text Skipgram Model](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5-skipgram.txt.bz2)

#### FastText

- [CBOW Model](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5-skipgram-cbow.model.tar.bz2)
- [Skipgram Model](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/SBW-vectors-300-min5-skipgram-fasttext.model.tar.bz2)


Corpora
-------

Most of the data comes from two soruces:

- [The Open Parallel Corpus Project (OPUS)](http://opus.nlpl.eu/): This is a
  resource built for the purpose of machine translation tasks.
- [Wikimedia dump](https://dumps.wikimedia.org/): This version comes from a
  dump of November 20th, 2018. It was parsed with the help of [Wikipedia
  Extractor](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor)

There are also two resources I compiled myself that were added to the corpus:

- An extract of projects from 2011 to 2016 of the [Honorable Cámara de
  Diputados de la Nación Argentina](https://www.hcdn.gob.ar/).
- The [InfoLEG](http://www.infoleg.gob.ar/) corpus comprised of laws and
  regulations of the Republic of Argentina.

### Disclaimer

I tried to find all the Spanish corpora, from different sources, that were
available to download freely from the web. No copyright infringement was
intended and I also tried to acknowledge correctly all the original authors of
the corpora I borrowed.

If you are an author of one of the resources and feel your work wasn't
correctly used in this resource please feel free to [contact
me](mailto:ccardellino@unc.edu.ar) and I will remove your work from this corpus
and from the embeddings.

Likewise, if you are author or know of some other resources publicly available
for the Spanish language (the corpus doesn't need to be annotated) and want to
contribute, also feel free to contact me.

Corpus Processing Tools
-----------------------

The [github repository of the SBWCE](https://github.com/crscardellino/sbwce) has
the set of tools I used to download and process the corpus. In particular, it has
the list of all the resources I used. I use the following scripts (and order)
to compile the data. You are welcome to contribute (most of these scripts are
not really optimized and were done in a rush).

### Download copora

The scripts that download corpora are: `download_unlabeled_corpora.sh`, which
downloads the corpora in the list `unlabeled_corpora.tsv`; `get_hcdn.py`
which download the corpus of the "Honorable Cámara de Diputados"; and
`get_infoleg.py` which downloads the "InfoLEG corpus".

### Process corpora

In order to process the corpora, the first script to use is
`extract_wikimedia.sh`, which uses the "Wikipedia Extractor" to remove tags
from the wikimedia corpus files downloaded in the previous step.

Then you can use the script `parse_corpus.py` which uses Spacy to tokenize,
sentence split, lemmatize and tag the whole corpora, resulting in what can be
found on the "Tagged Corpus".

### Clean corpora

After having parsed the corpora, the next step is to try to find and remove
duplicated sentences, and making sure the corpus is ready for training the
word embeddings. In order to do this, you need first to run the
`clean_corpus.sh` script that will take the tagged corpora from the previous
step and return a single file where each line is a single sentence from the
corpus. Then you can run the `remove_dups.py` script in order to remove all
those duplicated sentences from the corpus.

### Embeddings training

For training the embeddings you can run either of the scripts `fasttext.py` or
`word2vec.py`.

Description of Resulting Embeddings
-----------------------------------

The original corpus had the following amount of data:

* A total of 2024959560 raw words.
* A total of 95820578 sentences.
* A total of 9157394 unique tokens.

After the models were trained, filtering of words with less than 5
occurrences as well as the downsample of the 27 most common words, the
following values were obtained:

* A total of 1510908618 raw words.
* A total of 1820142 unique tokens.

The final resource was a corpus of 1820142 word embeddings of dimension 300.

Citation
--------

To cite this resource in a publication please use the following citation:

> Cristian Cardellino: Spanish Billion Words Corpus and Embeddings (August
> 2019), https://crscardellino.github.io/SBWCE/

You also have a [bibtex](cite.bib) entry available.

License
-------

<div style="text-align: center;">
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img
alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
<span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Spanish Billion Word
Corpus and Embeddings</span>
by <span xmlns:cc="http://creativecommons.org/ns#"
property="cc:attributionName">Cristian Cardellino</span><br />
is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative
Commons Attribution-ShareAlike 4.0 International License</a>.
</div>
