from ch3_deque import *


def palindromeChecker(s):
    s.replace(" ","")
    charDeque = Deque()
    for ch in s:
        charDeque.addRear(ch)
    stillEqual = True
    while (charDeque.size() > 1) and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        stillEqual = (first == last)
    return stillEqual
