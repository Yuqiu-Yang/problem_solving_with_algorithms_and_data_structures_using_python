def dpMakeChange(coinValueList, change):
    if min(coinValueList) != 1:
        raise ValueError("Min coin value has to be 1")

    minCoins = [0] * (change + 1)
    coinsUsed = [0] * (change + 1)
    for cents in range(1,change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 <= coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j

        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change], minCoins, coinsUsed

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        print(coinsUsed[coin])
        coin -= coinsUsed[coin]


a,b,c =dpMakeChange([1,5,10,21,25],63)
print(a)
print(b)
print(c)
printCoins(c, 63)
printCoins(c, 52)



a,b,c =dpMakeChange([1,5,8,10,25],33)
print(a)
print(b)
print(c)
printCoins(c, 33)
