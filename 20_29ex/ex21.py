import re
from ex20 import extract_wikidocs

def main():
    wiki_docs = extract_wikidocs()
    for doc in wiki_docs:
        lines = doc['text'].split('\n')
        for line in lines:
            if re.search(ur'\[\[Category:.*?\]\]', line):
                print line.encode('utf-8')

if __name__ == '__main__':
    main()