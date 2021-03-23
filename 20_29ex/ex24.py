import re
from ex20 import extract_wikidocs

def main():
    docs = extract_wikidocs()
    pattern = re.compile(ur'(File|ファイル):([^\|]+)')
    for doc in docs:
        references = pattern.findall(doc['text'])
        for ref in references:
            print ref[1].encode('utf-8')
            
if __name__ == '__main__':
    main() 