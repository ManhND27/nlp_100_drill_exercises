from nltk.tokenize import word_tokenize
import string
import re

def char_count(w): 
    num = 0
    for i in range(len(w)):
        if re.search(r'[a-zA-Z]',w[i]):
            num += 1
    return num

def get_num_chars(words):
    list1 = []

    for w in words: 
        list1.append(char_count(w))

    return list1

if __name__ == '__main__':
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

    print ('Input string %s' % sentence)

    print ('__ using tokenizer')
    words = sentence.split()
    print (repr(words))
    print (repr(get_num_chars(words)))

    print ('__ using nltk for tokenizing')
    words = word_tokenize(sentence)
    print (repr(words))
    print (repr(get_num_chars(words)))