import re
from read_data_ex30 import read_data

if __name__ == '__main__':
    sentences = read_data()
    for sen in sentences:
        for morph in sen:
            if morph['pos'] == '名詞' and morph['pos1'] == 'サ変接続':
                print morph['surface']