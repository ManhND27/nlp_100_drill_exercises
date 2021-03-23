import re
import codecs

def read_file(filename):
    f = codecs.open(filename, 'rU')
    sentences = []
    morphemes = []
    for line in f:
        line = line.strip()
        if line == '':
            next
        elif line == 'EOS':
            if morphemes:
                sentences.append(morphemes)
            morphemes = []    
        else:
            morph = {}
            fields = line.split()
            surf     = fields[0]
            features = fields[1].split(',')
            pos  = features[0]
            pos1 = features[1]
            base = features[6]
            
            morph['surface'] = surf
            morph['base'] = base
            morph['pos']  = pos
            morph['pos1'] = pos1
            
            morphemes.append(morph)
    f.close()

    return sentences

def read_data():
    input_file = 'C:\Users\ThinkPro\Desktop\InternAimesoft_tutorial\nlp_100_drill_exercises\data\neko.txt'
    return read_file(input_file)

# print sentence information, which is the list of morphemes    
def print_sent_info(sen):
    print ("+ Number of morphemes: %s" % len(sen))
    for morph in sen:
        print ('  %s  %s,%s,%s' % (morph['surface'], morph['pos'], morph['pos1'], morph['base']))
    
if __name__ == '__main__':
    sentences = read_data()
    print ('Number of sentences: %s' % len(sentences))

    for i in xrange(5):
        sen = sentences[i]
        print_sent_info(sen)