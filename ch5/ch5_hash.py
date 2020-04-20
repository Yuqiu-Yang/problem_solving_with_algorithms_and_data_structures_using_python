def stringHash(aString, tableSize, weight = "None"):
    sum = 0
    if weight == "Positional":
        for pos in range(len(aString)):
            sum += ord(aString[pos]) * (pos + 1)
    elif weight == "Quadratic":
        for pos in range(len(aString)):
            sum += ord(aString[pos]) * ((pos + 1)**2)
    else:
        for pos in range(len(aString)):
            sum += ord(aString[pos])

    return sum%tableSize


print(stringHash("cat", 11, "Positional"))
