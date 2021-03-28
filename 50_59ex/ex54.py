from xml.dom import minidom
import os
import sys

if __name__ == '__main__':
    xmldoc = minidom.parse('../../data/nlp.txt.xml')
    token_list = xmldoc.getElementsByTagName('token')
    for tknode in token_list:
        info = []
        for tag in ['word', 'lemma', 'POS']:
            node = tknode.getElementsByTagName(tag)
            info.append(node[0].firstChild.data)
        print '\t'.join(info)