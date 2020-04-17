def stringDistance(newString, referenceString):
    m = len(newString)
    n = len(referenceString)
    dp_result = [[0]*(n + 1) for x in range(m+1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                # if the newString is empty we simply
                # insert characters
                dp_result[i][j] = i * 20
            elif j == 0:
                # if the referenceString is empty we simply
                # delete characters
                dp_result[i][j] = j * 20
            elif (newString[i - 1]) == (referenceString[j - 1]):
                # if the last characters of the two strings
                # match, we copy the character
                dp_result[i][j] = dp_result[i - 1][j - 1] + 5
            else:
                # we can first try insertion
                # then we try deletion
                dp_result[i][j] = min([dp_result[i][j - 1] + 20, \
                                        dp_result[i - 1][j] + 20])
    return dp_result

str1 = "algorithm"
str2 = "alligator"
print(stringDistance(str1, str2))
