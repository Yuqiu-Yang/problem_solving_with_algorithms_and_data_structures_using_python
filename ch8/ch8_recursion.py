import random
def encrypt(m, k):
    s = "abcdefghijklmnopqrstuvwxyz"
    n = ''
    for i in m:
        j = (s.find(i) + k)%26
        n = n + s[j]
    return n

def decrypt(m, k):
    s = "abcdefghijklmnopqrstuvwxyz"
    n = ""
    for i in m:
        j = (s.find(i) - k)%26
        n = n + s[j]
    return n

def modExpIte(x, n, p):
    tmp = 1
    for i in range(n):
        tmp *= x
        tmp %= p
    return tmp

def modExpRec(x, n, p):
    if n == 0:
        return 1
    t = (x ** 2)%p
    tmp = modExpRec(t, n // 2, p)
    if n % 2 != 0:
        tmp = (x * tmp) % p
    return tmp

def gcdOriginal(a, b):
    if b == 0:
        return a
    elif a < b:
        return gcdOriginal(b, a)
    else:
        return gcdOriginal(a - b, b)

def gcdModular(a, b):
    if b == 0:
        return a
    else:
        return gcdModular(b, a % b)

def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x%y)
        return (d, b, a - (x//y)*b)


def toChunks(m, chunkSize):
    byteMess = bytes(m, 'utf-8')
    # byteMess gives ASCII values for each character in m
    hexString = ''
    for b in byteMess:
        hexString = hexString + ("%02x" % b)
    chunkList = []
    # every character can be represented by 2 hexadecimal number with a possible leading 0
    for i in range(0, len(hexString), 2 * chunkSize):
        chunkList.append(hexString[i : (i + 2*chunkSize)])
    chunkList = [eval('0x' + x) for x in chunkList if x]
    return chunkList

def chunksToPlain(clist, chunkSize):
    hexList = []
    for c in clist:
        hexString = hex(c)[2:]
        clen = len(hexString)
        hexList.append('0'* ((2*chunkSize - clen) %2)  + hexString)
    hstring = ''.join(hexList)
    messArray = bytearray.fromhex(hstring)
    return messArray.decode('utf-8')


def RSAgenKeys(p, q):
    n = p * q
    # Euler totient function
    pqminus = (p - 1) * (q - 1)
    e = int(random.random() * n)
    while gcdModular(pqminus, e) != 1:
        e = int(random.random() * n)
    d, a, b = ext_gcd(pqminus, e)
    d = b
    if d < 0:
        d += pqminus
    return (e, d, n)


def RSAencrypt(m, e, n):
    ndigits = n.bit_length()
    # chunkSize is the max number of characters in a chunk
    chunkSize = ndigits // 8
    chunks = toChunks(m, chunkSize)
    encList = []
    for messChunk in chunks:
        c = modExpRec(messChunk, e, n)
        encList.append(c)
    return encList, chunkSize

def RSAdecrypt(clist, d, n):
    rList = []
    for c in clist:
        m = modExpRec(c, d, n)
        rList.append(m)
    return rList



m = 'goodbye girl'
e, d, n = RSAgenKeys(5563, 8191)
c, c_size = RSAencrypt(m, e, n)
m1 = RSAdecrypt(c, d, n)
print(chunksToPlain(m1, c_size))
