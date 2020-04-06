from ch3_stack import Stack

def decimalToBaseInt(decNumber, base):
    digits = "0123456789ABCDEF"
    if (base <= 1) or (base > 16):
        raise RuntimeError("Inproper base value")
    decNumber = int(decNumber)

    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    baseString = ''
    while not remstack.isEmpty():
        baseString += digits[remstack.pop()]

    return baseString

def baseToDecimalInt(baseNumber, base):
    digits = "0123456789ABCDEF"
    if (base <= 1) or (base > 16):
        raise RuntimeError("Inproper base value")
    baseNumber = str(baseNumber)
    l = len(baseNumber)
    decNumber = 0
    for i in range(l):
        temp = digits.index(baseNumber[l - i - 1])
        decNumber += (temp* (base**i))

    return decNumber


def baseToBaseInt(baseNumber, fromBase, toBase):
    if (fromBase <= 1) or (fromBase > 16):
        raise RuntimeError("Inproper base value")
    if (toBase <= 1) or (toBase > 16):
        raise RuntimeError("Inproper base value")
    decNumber = baseToDecimalInt(str(baseNumber), fromBase)
    toBaseNumber = decimalToBaseInt(decNumber, toBase)

    return toBaseNumber

def seperateParts(numString):
    numString = str(numString)
    if not ("." in numString):
        numString += ".0"
    return int(numString.split(".")[0]), \
    float("0."+numString.split(".")[1])

def decimalToBaseDecimal(decNumber, base, precision):
    if (base <= 1) or (base > 16):
        raise RuntimeError("Inproper base value")
    digits = "0123456789ABCDEF"
    s = Stack()
    decNumber = float(decNumber)
    for i in range(precision):
        decNumber *= base
        intPart, decNumber = seperateParts(decNumber)
        s.push(intPart)

    baseString = ''
    while not s.isEmpty():
        baseString += digits[s.pop()]
    return baseString[(precision-1):0:-1]

def baseToDecimalDecimal(baseNumber, base):
    digits = "0123456789ABCDEF"
    if (base <= 1) or (base > 16):
        raise RuntimeError("Inproper base value")
    baseNumber = str(baseNumber).split(".")[1]
    l = len(baseNumber)
    decNumber = 0
    for i in range(l):
        temp = digits.index(baseNumber[i])
        decNumber += (temp* (base**(-i - 1)))

    return decNumber

def baseToBaseDecimal(baseNumber, fromBase, toBase, precision):
    if (fromBase <= 1) or (fromBase > 16):
        raise RuntimeError("Inproper base value")
    if (toBase <= 1) or (toBase > 16):
        raise RuntimeError("Inproper base value")
    decNumber = baseToDecimalDecimal(str(baseNumber), fromBase)
    toBaseNumber = decimalToBaseDecimal(decNumber, toBase, precision)

    return toBaseNumber


def baseToBase(baseNumber, fromBase, toBase, precision):
    if (fromBase <= 1) or (fromBase > 16):
        raise RuntimeError("Inproper base value")
    if (toBase <= 1) or (toBase > 16):
        raise RuntimeError("Inproper base value")
    intPart, decPart = seperateParts(baseNumber)
    intString  = baseToBaseInt(intPart, fromBase, toBase)
    decString = baseToBaseDecimal(decPart, fromBase, toBase, precision)

    return intString + "." + decString
