
import os
import sys
import re
from xml.dom import minidom

def get_mention_txt(rep_node):
    txtnode = rep_node.getElementsByTagName('text')
    txt = txtnode[0].firstChild.data
    txt = re.sub(r'-LRB-', '(', txt)
    txt = re.sub(r'-RRB-', ')', txt)
    return txt

if __name__ == '__main__':
    xmldoc = minidom.parse('../../data/nlp.txt.xml')
    root_coref  = xmldoc.getElementsByTagName('coreference')[0]
    coref_nodes = root_coref.getElementsByTagName('coreference')

    for node in coref_nodes:
        mention_nodes = node.getElementsByTagName('mention')
        rep_node = mention_nodes[0]
        rep_txt = get_mention_txt(rep_node)
        for mm in mention_nodes[1:]:
            txt = get_mention_txt(mm)
            print '%s (%s)' % (txt, rep_txt)