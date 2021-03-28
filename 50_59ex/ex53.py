import os
import sys
import re

if __name__ == '__main__':
    with open('../data/nlp.txt.xml', 'rU') as f:
        for line in f:
            line = line.strip()
            match = re.match(r'<word>(.+)</word>', line)
            if match:
                print (match.group(1))
        