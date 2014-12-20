#!/usr/bin/python3

import sys, os
import nltk

if len(sys.argv) < 2:
    print("Please supply a filename.")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as f:
    data = f.read()

# Break the input down into sentences, then into words, and position tag
# those words.
raw_sentences = nltk.sent_tokenize(data)
sentences = [nltk.pos_tag(nltk.word_tokenize(sentence)) \
    for sentence in raw_sentences]

# Define a grammar, and identify the noun phrases in the sentences.
chunk_parser = nltk.RegexpParser(r"NP: {((<DT>|<PRP\$>)?<JJ>*(<NN>|<NNP>)+|<PRP>)}")

trees = [chunk_parser.parse(sentence) for sentence in sentences]

for index, tree in enumerate(trees):
    print("===\nSentence: %s\nNoun phrases:" %
            raw_sentences[index].replace('\n', ' '))
    for subtree in tree.subtrees(filter = lambda t: t.label() == 'NP'):
        print("  %s" % subtree)
