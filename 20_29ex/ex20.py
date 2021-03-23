# -*- coding: utf-8 -*-

import gzip
import sys
import json
import codecs
import re

def extract_wikidocs():
    filename = '../data/jawiki-country.json.gz'
    f = gzip.open(filename, 'rU')
    wiki_docs = []
    for line in f:
        line = line.rstrip()
        doc = json.loads(line, 'utf-8')
        if re.search(ur'イギリス', doc['text']):
            wiki_docs.append(doc)    
    f.close()

    return wiki_docs

def main():
    wiki_docs = extract_wikidocs()
    print '# Wikipedia articles related to イギリス: %s' % len(wiki_docs)
    for doc in wiki_docs:
        print doc['title'].encode('utf-8')
        print doc['text'].encode('utf-8')

if __name__ == '__main__':
    main()