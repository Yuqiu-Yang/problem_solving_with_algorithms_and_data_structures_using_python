from ch3_stack import Stack

def match(open_par, close_par):
    opens = '([{'
    closes = ')]}'
    return opens.index(open_par) == closes.index(close_par)


def parentheses_checker(par_string):
    s = Stack()
    isBalanced = True
    index = 0
    while (index < len(par_string)) and (isBalanced):
        symbol = par_string[index]
        if symbol in ['(','[','{']:
            s.push(symbol)
        else:
            if (s.isEmpty()) or (not match(s.peek(), symbol)):
                isBalanced = False
            else:
                s.pop()
        index += 1
    return (isBalanced) and (s.isEmpty())
