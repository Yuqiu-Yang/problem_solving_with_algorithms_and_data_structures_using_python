from ch3_stack import *

def htmlChecker(htmlFilePath):
    htmlFile = open(htmlFilePath)
    htmlList = htmlFile.read().split()
    htmlFile.close()
    htmlStack = Stack()
    isBalanced = True
    while (len(htmlList) != 0) and isBalanced:
        temp = htmlList.pop(0)
        #print(temp)
        if isHTMLTag(temp):
            if (temp[1] != "/"):
                # if opening tag
                htmlStack.push(temp)
            else:
                if htmlStack.size() == 0:
                    isBalanced = False
                else:
                    # if close tag
                    isBalanced = ((htmlStack.peek()) == \
                            (temp.replace("/","")))
                    htmlStack.pop()


    return isBalanced





def isHTMLTag(tagString):
    l = len(tagString)
    if (tagString[0] == "<") and (tagString[l - 1] == ">"):
        return True
    else:
        return False
