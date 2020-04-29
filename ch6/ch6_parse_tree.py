from ch3_stack import *
from ch6_binary_tree import *
import operator
import string
import re
def expProcessor(fpexp):
    temp = re.findall('[0-9.a-zA-Z]+|[**]+|[//]+|[+\-*/()]?|[not]?|[and]?|[or]?|[True]?|[False]?|.',\
    fpexp)
    fplist = [i for i in temp if i not in ["", " "]]
    i = 1
    while True:
        if (fplist[i] == "-") and (fplist[i-1] in ["(","+","-","*","/","**","//","not","and","or"]):
            fplist[i+1] = "-"+fplist[i+1]
            fplist.pop(i)
        else:
            i += 1
            if i >= len(fplist)-1:
                break
    return fplist





def buildParseTree(fplist):
    pStack = Stack()
    eTree = BinaryTree("")
    pStack.push(eTree)
    currentTree = eTree
    for i in range(len(fplist)):
        if fplist[i] == "(":
            currentTree.insertLeft("")
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif fplist[i] == ")":
            currentTree = pStack.pop()
        elif fplist[i] in ["+","-", "*", "/","**","//", "not", "or", "and"]:
            if fplist[i] == "not":
                currentTree = pStack.pop()
            currentTree.setRootVal(fplist[i])
            currentTree.insertRight("")
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        else:
            if fplist[i] in string.ascii_letters:
                currentTree.setRootVal(fplist[i])
            else:
                currentTree.setRootVal(eval(fplist[i]))
            currentTree = pStack.pop()

    return eTree

def deriv(parseTree, val):
    operslist = ["+", "-", "*", "/", "**"]
    # we only deal with +, -, *, /, **
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        if parseTree.getRootVal() in ["+", "-"]:
            if (leftC.getRootVal() == val) and (not rightC.getRootVal() in (operslist + [val])):
                # if x +- 0
                return f"(1)"
            elif (not leftC.getRootVal() in (operslist + [val])) and (rightC.getRootVal() == val):
                # if 0 +- x
                if parseTree.getRootVal() == "+":
                    return f"(1)"
                else:
                    return f"(-1)"
            elif (not leftC.getRootVal() in (operslist + [val])) and (not rightC.getRootVal() in (operslist + [val])):
                # if 0 +- 0
                return f"(0)"
            elif (leftC.getRootVal() == val) and (rightC.getRootVal() == val):
                # if x +- x
                if parseTree.getRootVal() == "+":
                    return f"(2)"
                else:
                    return f"(0)"
            elif (leftC.getRootVal() in operslist) and (rightC.getRootVal() in operslist):
                # if fx +- gx
                return f"({deriv(leftC,val)} {parseTree.getRootVal()} {deriv(rightC, val)})"
            elif (leftC.getRootVal() == val) and (rightC.getRootVal() in operslist):
                # if x +- gx
                return f"(1 {parseTree.getRootVal()} {deriv(rightC, val)})"
            elif (leftC.getRootVal() in operslist) and (rightC.getRootVal() == val):
                # if fx +- x
                return f"({deriv(leftC, val)} {parseTree.getRootVal()} 1)"
            elif (leftC.getRootVal() in operslist) and (not rightC.getRootVal() in (operslist + [val])):
                # if fx +- 0
                return f"({deriv(leftC, val)})"
            elif (not leftC.getRootVal() in (operslist + [val])) and (rightC.getRootVal() in operslist):
                # if 0 +- gx
                return f"({parseTree.getRootVal()}{deriv(rightC, val)})"
        elif parseTree.getRootVal() == "*":
            if (leftC.getRootVal() == val) and (not rightC.getRootVal() in (operslist + [val])):
                # if x * 0
                return f"({rightC.getRootVal()})"
            elif (not leftC.getRootVal() in (operslist + [val])) and (rightC.getRootVal() == val):
                # if 0 * x
                return f"({leftC.getRootVal()})"
            elif (not leftC.getRootVal() in (operslist + [val])) and (not rightC.getRootVal() in (operslist + [val])):
                # if 0 * 0
                return f"(0)"
            elif (leftC.getRootVal() == val) and (rightC.getRootVal() == val):
                # if x * x
                return f"(2 * x)"
            elif (leftC.getRootVal() in operslist) and (rightC.getRootVal() in operslist):
                # if fx * gx
                return f"({printExp(leftC)}*{deriv(rightC, val)} + {deriv(leftC, val)}*{printExp(rightC)})"
            elif (leftC.getRootVal() == val) and (rightC.getRootVal() in operslist):
                # if x * gx
                return f"({val}*{deriv(rightC, val)} + {printExp(rightC)})"
            elif (leftC.getRootVal() in operslist) and (rightC.getRootVal() == val):
                # if fx * x
                return f"({printExp(leftC)} + {deriv(leftC, val)}*{val})"
            elif (leftC.getRootVal() in operslist) and (not rightC.getRootVal() in (operslist + [val])):
                # if fx * 0
                return f"({rightC.getRootVal()} * {deriv(leftC, val)})"
            elif (not leftC.getRootVal() in (operslist + [val])) and (rightC.getRootVal() in operslist):
                # if 0 * gx
                return f"({leftC.getRootVal()} * {deriv(rightC, val)})"
        elif parseTree.getRootVal() == "/":
            if (leftC.getRootVal() == val) and (not rightC.getRootVal() in (operslist + [val])):
                # if x / 0
                return f"(1/({rightC.getRootVal()}))"
            elif (not leftC.getRootVal() in (operslist + [val])) and (rightC.getRootVal() == val):
                # if 0 / x
                return f"((-1*({leftC.getRootVal()}))/({val}**2))"
            elif (not leftC.getRootVal() in (operslist + [val])) and (not rightC.getRootVal() in (operslist + [val])):
                # if 0 / 0
                return f"(0)"
            elif (leftC.getRootVal() == val) and (rightC.getRootVal() == val):
                # if x / x
                return f"(0)"
            elif (leftC.getRootVal() in operslist) and (rightC.getRootVal() in operslist):
                # if fx / gx
                return f"((({deriv(leftC, val)})*({printExp(rightC)}) - ({printExp(leftC)}))/(({printExp(rightC, val)})**2))"
            elif (leftC.getRootVal() == val) and (rightC.getRootVal() in operslist):
                # if x / gx
                return f"((({printExp(rightC)}) - ({printExp(leftC)}) ) / (({printExp(rightC, val)})**2))"
            elif (leftC.getRootVal() in operslist) and (rightC.getRootVal() == val):
                # if fx / x
                return f"(({deriv(leftC, val)}) * {val} - ({printExp(leftC)}))"
            elif (leftC.getRootVal() in operslist) and (not rightC.getRootVal() in (operslist + [val])):
                # if fx / 0
                return f"(({deriv(leftC, val)})/ ({rightC.getRootVal}))"
            elif (not leftC.getRootVal() in (operslist + [val])) and (rightC.getRootVal() in operslist):
                # if 0 / fx
                return f"((-1) * ({leftC.getRootVal()}) / (({printExp(rightC)})**2))"

        elif parseTree.getRootVal() == "**":
            if (leftC.getRootVal() == val) and (not rightC.getRootVal() in (operslist + [val])):
                # if x ** 0
                if rightC.getRootVal() == 0:
                    return f"(0)"
                else:
                    return f"(({rightC.getRootVal()}) * (({val}) ** ({rightC.getRootVal()} - 1)))"
            elif (not leftC.getRootVal() in (operslist + [val])) and (rightC.getRootVal() == val):
                # if 0 ** x
                return f"((({leftC.getRootVal()}) ** ({val})) * (ln({leftC.getRootVal()})))"
            elif (not leftC.getRootVal() in (operslist + [val])) and (not rightC.getRootVal() in (operslist + [val])):
                # if 0 ** 0
                return f"(0)"
            elif (leftC.getRootVal() == val) and (rightC.getRootVal() == val):
                # if x ** x
                return f"(({val}**{val}) * (ln({val}) + 1))"
            elif (leftC.getRootVal() in operslist) and (rightC.getRootVal() in operslist):
                # if fx ** gx
                return f"( (({printExp(leftC)}) ** ({printExp(rightC)}))  *  ( (({printExp(rightC)} * ({deriv(leftC, val)}))/({printExp(leftC)})) +  (({deriv(rightC, val)}) * (ln({printExp(leftC)})))))"
            elif (leftC.getRootVal() == val) and (rightC.getRootVal() in operslist):
                # if x ** gx
                return f"( (({val}) ** ({printExp(rightC)})) * ((({deriv(rightC, val)}) * ln({val}))  + (({printExp(rightC)}) / x)) )"
            elif (leftC.getRootVal() in operslist) and (rightC.getRootVal() == val):
                # if fx ** x
                return f"( (({printExp(leftC)}) ** ({val})) * ((ln({printExp(leftC)})) + ( (({val}) * ({deriv(leftC, val)}))/ ({printExp(leftC)}))))"
            elif (leftC.getRootVal() in operslist) and (not rightC.getRootVal() in (operslist + [val])):
                # if fx ** 0
                if rightC.getRootVal() == 0:
                    return f"(0)"
                else:
                    return f"( (({printExp(leftC)})**({rightC.getRootVal()})) * (({rightC.getRootVal()}) * ({deriv(leftC, val)})/({printExp(leftC)})))"
            elif (not leftC.getRootVal() in (operslist + [val])) and (rightC.getRootVal() in operslist):
                # if 0 ** gx
                return f"( (({leftC.getRootVal()}) ** ({printExp(rightC)})) * (ln({leftC.getRootVal()}) * ({deriv(rightC, val)}))  )"


def evaluate(parseTree):
    opers = {"+": operator.add, "-": operator.sub,
              "*": operator.mul, "/": operator.truediv,
              "**": operator.pow, "//": operator.floordiv,
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
              "**": operator.pow, "//": operator.floordiv,
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
