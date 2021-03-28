from xml.dom import minidom

class Node:
    def __init__(self, lb, text=None):
        self.label    = lb
        self.children = []
        self.text     = text

    def is_leaf():
        return len(self.children) == 0

    def children(self):
        return self.children
        
    def to_s(self):
      
   
        return ' '

def parse_s_exp(s_exp):
 

    stack = []
    i = 0
    par
    while ( i < len(s_exp) ):
        if s_exp[i] == '(':
            i += 1
            stack.append(s_exp[i])
            lb = ''
            while i < len(s_exp) and s_exp[i] != ' ' and s_exp[i] != ')':
                lb += s_exp[i]
                i += 1
            print ('label = %s' % lb)
            stack.append(lb)
        elif s_exp[i] == ')':
            i += 1
            stack.append(s_exp[i])
        elif s_exp[i] == ' ':
            i += 1
        else:
            txt = ''
            while i < len(s_exp) and s_exp[i] != ' ' and s_exp[i] != ')':
                txt += s_exp[i]
                i += 1
            if len(stack) > 0 and stack[-1] != ')' and stack[-1] != '(':
                lb = stack.pop()
                node = Node(lb, txt)
                # print ('leaf node: label = %s text = %s' % (lb, txt))
    
if __name__ == '__main__':
   xmldoc   = minidom.parse('../data/nlp.txt.xml')
   xmlnodes = xmldoc.getElementsByTagName('parse')

   for xmlnode in xmlnodes:
       s_exp = xmlnode.firstChild.data
       sen_node = parse_s_exp(s_exp)