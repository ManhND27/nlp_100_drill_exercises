def main():
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

    words = sentence.split()
    char_dict = {}

    keys = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    index_dict = {key: None for key in keys}

    for i in range(len(words)):
        w = words[i]
        if i+1 in index_dict:
            char_dict[w[0]] = i+1
        else:
            char_dict[''.join(w[0:2])] = i+1

    print ('Input sentense: %s' % sentence)
    print (repr(words))
    print (repr(char_dict))

if __name__ == '__main__':
    main()
