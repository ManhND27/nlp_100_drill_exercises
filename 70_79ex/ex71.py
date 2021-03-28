def read_stopwords(filename):
    stopdict = {}
    f = open(filename, 'rU')
    for line in f:
        w = line.strip()
        if w == '': continue
        stopdict[w] = 1
    f.close()
    return stopdict

stopdict = read_stopwords('../../data/stopword.txt')    

def is_stopword(w):
    if stopdict.has_key(w):
        return True
    else:
        return False

def test(w, expected):
    got = is_stopword(w)
    if got == expected:
        print ' OK  %s\t%s' % (w, got)
    else:
        print '  X  %s\t%s' % (w, got)

def main():
    test('able', True)
    test('above', True)
    test('yourselves', True)
    test('man', False)
    test('home', False)
    test("you're", True)

if __name__ == '__main__':
    main()