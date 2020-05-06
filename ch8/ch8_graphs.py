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
