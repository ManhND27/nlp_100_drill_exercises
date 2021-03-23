from ex05 import get_char_ngrams

def main():
    s1 = 'paraparaparadise'
    s2 = 'paragraph'

    X = set(get_char_ngrams(s1,2))
    Y = set(get_char_ngrams(s2,2))

    print (s1)
    print (s2)

    print ('X = %s' % X)
    print ('Y = %s' % Y)

    union = X.union(Y)
    intersection = X.intersection(Y)
    difference = X.difference(Y)

    print ('union  : %s' % union)
    print ('intersection: %s' % intersection)
    print ('difference: %s' % difference)

    brg = 's e'
    if brg in X:
        print('%s is in X' % brg)
    else : 
        print('%s is not in X' % brg)

    if brg in Y:
         print('%s is in Y' % brg)
    else : 
        print('%s is not in Y' % brg)

if __name__ == '__main__':
    main()
