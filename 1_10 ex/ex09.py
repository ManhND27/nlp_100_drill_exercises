import random

def typoglycemia(s):
    news = []
    words = s.split()
    for w in words:
        news.append(process(w))
    return ' '.join(news)

def process(w):
    if len(w) < 4:
        return w

    neww = w[0]
    random_index = list(range(1,len(w)))

    random.shuffle(random_index)
    for i in random_index:
        neww += w[i]
        
    neww += w[-1]
    return neww
    
def main():
    random.seed(999)
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    print ("Original string: %s" % s)
    print ("Typoglycemia string: %s" % typoglycemia(s))


if __name__ == '__main__':
    main()    
    

    