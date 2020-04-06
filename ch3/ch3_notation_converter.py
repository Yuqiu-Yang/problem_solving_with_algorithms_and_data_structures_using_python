from ch3_stack import Stack
from ch3_parentheses_checker import parentheses_checker
import string


def infixStringCheck(infixExpr):
    tokenList = " ".join(infixExpr).split()
    parString = ""
    s = Stack()
    for i in range(len(tokenList)):
        if tokenList[i] in "([{}])":
            parString += tokenList[i]
            tokenList[i] = " "
        else:
            s.push(tokenList[i])
    if not parentheses_checker(parString):
        return False
    else:
        while not s.isEmpty():
            temp = s.pop()
            if not ((temp in string.ascii_letters) or \
            (temp in "0123456789")):
                return False
            else:
                if s.isEmpty():
                    return True
                else:
                    if not s.peek() in "+-*/":
                        return False
                    else:
                        s.pop()


def infixToPostfix(infixExpr):
    if not infixStringCheck(infixExpr):
        raise RuntimeError("Incorrect Infix Expression")
    operatorStack = Stack()
    operatorDic = {}
    operatorDic["*"] = 3
    operatorDic["/"] = 3
    operatorDic["+"] = 2
    operatorDic["-"] = 2
    operatorDic["("] = 1

    postfixList = []

    tokenList = " ".join(infixExpr).split()

    for token in tokenList:
        if (token in string.ascii_letters) or \
        (token in "0123456789"):
            postfixList.append(token)
        elif token == "(":
            operatorStack.push(token)
        elif token == ")":
            while operatorStack.peek() != "(":
                postfixList.append(operatorStack.pop())
            operatorStack.pop()
        else:
            while (not operatorStack.isEmpty()) and \
            (operatorDic[operatorStack.peek()] >= operatorDic[token]):
             postfixList.append(operatorStack.pop())
            operatorStack.push(token)

    while not operatorStack.isEmpty():
        postfixList.append(operatorStack.pop())

    return " ".join(postfixList)

def revExpr(expr):
    s = Stack()
    tokenList = " ".join(expr).split()
    for token in tokenList:
        if token == "(":
            s.push(")")
        elif token == ")":
            s.push("(")
        else:
            s.push(token)
    revString = ""
    while not s.isEmpty():
        revString += s.pop()
    return revString

def infixToPrefix(infixExpr):
    revString = revExpr(infixExpr)
    revprefixString = infixToPostfix(revString)
    return revExpr(revprefixString)



def postfixToInfix(postfixExpr):
    operandStack = Stack()
    tokenList = " ".join(postfixExpr).split()
    for token in tokenList:
        if (token in string.ascii_letters) or \
        (token in "0123456789"):
            operandStack.push(token)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            tempString = f"({operand1} {token} {operand2})"
            operandStack.push(tempString)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = " ".join(postfixExpr).split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            temp = doMath(token, operand1, operand2)
            operandStack.push(temp)
    return operandStack.pop()


def lessThan_10_calculator(infixExpr):
    postfixExpr = infixToPostfix(infixExpr)
    return postfixEval(postfixExpr)
