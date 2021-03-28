from nltk.stem.snowball import SnowballStemmer
import sys
import codecs

stemmer = SnowballStemmer(u'english')

for w in sys.stdin:
    w = w.strip()
    if w == '':
        print 
    else:
        wstem = stemmer.stem(w.decode('utf-8', errors='ignore'))
        print ('%s\t%s' % (w, wstem))