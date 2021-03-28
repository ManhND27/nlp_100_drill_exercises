import os
import sys
import re
from xml.dom import minidom
from collections import defaultdict

def get_id_n_text(node):
    idx = int(node.attributes['idx'].value)
    txt = node.firstChild.data
    return idx, txt

if __name__ == '__main__':
    xmldoc   = minidom.parse('../../data/nlp.txt.xml')
    xmlnodes = []
    for node in xmldoc.getElementsByTagName('dependencies'):
        if node.attributes['type'].value == 'collapsed-dependencies':
            xmlnodes.append(node)

    for node in xmlnodes:
        tokens = {}
        dep_nodes = node.getElementsByTagName('dep')
        
        predicates = {}
        tuples = defaultdict(defaultdict)
        
        for dn in dep_nodes:
            rel  = dn.attributes['type'].value
            gov  = dn.getElementsByTagName('governor')[0]
            gov_id, gov_txt = get_id_n_text(gov)
            tokens[gov_id]  = gov_txt
            
            dep  = dn.getElementsByTagName('dependent')[0]
            dep_id, dep_txt = get_id_n_text(dep)
            tokens[dep_id] = dep_txt

            if rel == 'nsubj':
                tuples[gov_id]['subj']  = dep_id
            elif rel == 'dobj':
                tuples[gov_id]['dobj'] = dep_id

        for pid in tuples.keys():
            predicate = tokens[pid]
            if not tuples[pid].has_key('subj') or not tuples[pid].has_key('dobj'):
                continue
            
            sid = tuples[pid]['subj']
            oid = tuples[pid]['dobj']
            subject = tokens[sid]
            purpose = tokens[oid]
            print ('\t'.join([subject, predicate, purpose]))