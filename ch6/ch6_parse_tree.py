from ch3_stack import *
from ch6_binary_tree import *
import operator
import string

def expProcessor(fpexp):
    fplist = []
    i = 0
    figlist = [str(x) for x in range(10)]
    while i < (len(fpexp)):
        if fpexp[i] in ["(",")", "+","-","*","/"]:
            fplist.append(fpexp[i])
            i += 1
        elif fpexp[i] == " ":
            i += 1
        elif fpexp[i] in figlist:
            temp_str = fpexp[i]
            while (i < (len(fpexp))) and (fpexp[i + 1] in figlist):
                temp_str += fpexp[i + 1]
                i += 1
            fplist.append(temp_str)
            i += 1
        elif fpexp[i] in string.ascii_letters:
            temp_str = fpexp[i]
            while (i < (len(fpexp))) and (fpexp[i + 1] in string.ascii_letters):
                temp_str += fpexp[i + 1]
                i += 1
            if temp_str in ["not", "and", "or", "True", "False"]:
                fplist.append(temp_str)
                i += 1
            else:
                raise ValueError("Unreconignizable character")
        else:
            raise ValueError("Unreconignizable character")
    return fplist




def buildParseTree(fplist):
    pStack = Stack()
    eTree = BinaryTree("")
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == "(":
            currentTree.insertLeft("")
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i == ")":
            currentTree = pStack.pop()
        elif i in ["+","-", "*", "/", "not", "or", "and"]:
            if i == "not":
                currentTree = pStack.pop()
            currentTree.setRootVal(i)
            currentTree.insertRight("")
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        else:
            currentTree.setRootVal(eval(i))
            currentTree = pStack.pop()

    return eTree


def evaluate(parseTree):
    opers = {"+": operator.add, "-": operator.sub,
              "*": operator.mul, "/": operator.truediv,
              "not": operator.not_, "and": operator.and_,
              "or": operator.or_}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        if parseTree.getRootVal() == "not":
            return fn(evaluate(rightC))
        else:
            return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


def postorderEvaluate(parseTree):
    opers = {"+": operator.add, "-": operator.sub,
              "*": operator.mul, "/": operator.truediv,
              "not": operator.not_, "and": operator.and_,
              "or": operator.or_}
    leftC = None
    rightC = None

    if parseTree:
        leftC = postorderEvaluate(parseTree.getLeftChild())
        rightC = postorderEvaluate(parseTree.getRightChild())
        if leftC and rightC:
            fn = opers[parseTree.getRootVal()]
            if parseTree.getRootVal() == "not":
                return fn(rightC)
            else:
                return fn(leftC, rightC)
        else:
            return parseTree.getRootVal()

def printExp(parseTree):
    sVal = ""
    if parseTree:
        if parseTree.getLeftChild() == None:
            sVal += str(parseTree.getRootVal())
        else:
            sVal += '(' + printExp(parseTree.getLeftChild())
            sVal += str(parseTree.getRootVal())
            sVal += printExp(parseTree.getRightChild()) + ')'
    return sVal
