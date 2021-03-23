import string
import re

def cipher(s):
    news = ''
    for i in range(len(s)):
        news = s[i]
        if re.search(r'[a-z]',s[i]):
            newc = chr(219 - ord(s[i]))
        news += newc

    return news


def decipher(s):
    news = ''
    for i in range(len(s)):
        tempc = chr(219 - ord(s[i]))
        newc = s[i]
        if re.search(r'[a-z]',tempc):
            newc = tempc
        news += newc

    return news

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = ' X '

    print ('%s got: %s expected :%s' % (prefix,repr(got),repr(expected)))


def main():
    s = 'aBcDef123'
    z = cipher(s)
    print('Xâu mã hóa của %s là %s' % (s,z))

    orig = decipher(z)
    print('Xâu giải mã của %s là %s' % (z,orig))

if __name__ == '__main__':
    main()
