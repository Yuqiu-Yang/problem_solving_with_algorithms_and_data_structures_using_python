from copy import deepcopy
def simpleMatcher(pattern, text):
    starti = 0
    i = 0
    j = 0
    match = False
    stop = False
    while not match and not stop:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            starti += 1
            j = 0
            i = starti
        if j == len(pattern):
            match = True
        else:
            if i == len(text):
                stop = True
    if match:
        return i - j
    else:
        return -1

def simpleMatcherAll(pattern, text):
    text_copy = deepcopy(text)
    startInd = []
    i = 0
    while len(text_copy) >= len(pattern):
        starti = simpleMatcher(pattern, text_copy)
        if starti == -1:
            break
        else:
            if i == 0:
                i += starti
            else:
                i += starti + 1 
            startInd.append(i)
            text_copy = text_copy[(starti+1):]
    return startInd

#################
from pythonds.graphs.adjGraph import *

def mismatchLinks(pattern):
    augPattern = '0' + pattern
    links = {}
    links[1] = 0
    for k in range(2, len(augPattern)):
        s = links[k - 1]
        stop = False
        while s >= 1 and not stop:
            if augPattern[s] == augPattern[k - 1]:
                stop = True
            else:
                s = links[s]
        links[k] = s + 1
    return links

def buildKMPGraph(pattern):
    g = Graph()
    ## If the pattern is 'ACATA'
    # The augPattern is '0ACATA6'
    augPattern = '0' + pattern + f'{len(pattern) + 1}'
    for i in range(len(augPattern)):
        g.addVertex(i)
    links = mismatchLinks(pattern)
    for s in links.keys():
        g.addEdge(s, links[s],cost = 1)
    return g, augPattern

def KMPMatcher(pattern, text):
    g, augPattern = buildKMPGraph(pattern)
    currentState = g.getVertex(0)
    i=-1
    while i < len(text) and (currentState.getId() != (len(pattern) + 1)):
        if currentState.getId() == 0:

            currentState = g.getVertex(1)
            i += 1
        if augPattern[currentState.getId()] == text[i]:
            currentState = g.getVertex(currentState.getId() + 1)
            i += 1
        else:
            currentState = list(currentState.getConnections())[0]
    if currentState.getId() == (len(pattern) + 1):
        return i - (len(pattern))
    else:
        return -1
