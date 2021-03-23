import re
from ex20 import extract_wikidocs

def main():
    wiki_docs = extract_wikidocs()
    for doc in wiki_docs:
        lines = doc['text'].split('\n')
        for line in lines:
            categories = re.findall(ur'\[\[Category:(.+)\]\]', line)
            for match in categories:
                for cat in match.split('|'):
                    if not re.search(ur'[\* ]', cat):
                        print cat.encode('utf-8')

if __name__ == '__main__':
    main()    