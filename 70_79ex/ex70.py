def add_labels(lb, filename):
    f = open(filename, 'rU')
    lines = f.readlines()
    lines = map( lambda x: ' '.join([lb, x]), lines )
    f.close()
    return lines

def main():
    fo = open('../../data/sentiment.txt', 'w')

    lines = add_labels('+1',  '../../data/rt-polaritydata/rt-polarity.pos')
    lines += add_labels('-1', '../../data/rt-polaritydata/rt-polarity.neg')

    fo.write( ''.join(lines) )

    fo.close()

if __name__ == '__main__':
    main()