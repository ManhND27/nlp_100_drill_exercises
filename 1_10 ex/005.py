def get_ngrams(arr, n, delim = ' '):
    ngrams = []
    for i in range(len(arr)):
        _min = i 
        _max = _min + n - 1
        if _max >= len(arr):
            break

        ngrams.append(delim.join(arr[_min:_max+1]))

    return ngrams

def get_char_ngrams(s, n):
    chars = []
    chars[:0] = s

    chars.insert(0, '__BOS__')
    chars.append('__EOS__')

    return get_ngrams(chars,2)

def get_word_ngrams(s, n):
    words = s.split()
    words.insert(0, '__BOS__')
    words.append('__EOS__')

    return get_ngrams(words, 2, '/')

def main():
    s = 'I am an NLPer'

    word_biagrams = get_word_ngrams(s, 2)
    char_biagrams = get_char_ngrams(s, 2)

    print ('input string: %s' % s)
    print('word bi-grams')
    print(word_biagrams)
    print('charactere bi-grams')
    print(char_biagrams)

if __name__ == '__main__':
    main()