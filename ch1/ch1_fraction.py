import math
import numpy as np
def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return int(n)

def lcm(m, n):
    return m*n//gcd(m,n)


def coprime(m,n):
    temp = gcd(m, n)
    while(temp != 1):
            m/=temp
            n/=temp
            temp = gcd(m, n)
    return int(m),int(n)


class Fraction(object):
    def __init__(self, top, bottom):
        if not (isinstance(top, int) and (isinstance(bottom, int))):
            raise RuntimeError("Error: BOTH NUMERATOR AND DENUMBERATOR NEED TO BE INTEGER")
        elif bottom == 0:
            raise RuntimeError("Error: The DENUMBERATOR CAN NOT BE 0")
        else:
            if top == 0:
                self.num, self.denum = 0, 1
            elif (top * bottom) < 0 :
                self.num, self.denum = coprime(abs(top), abs(bottom))
                self.num *= -1
            else:
                self.num, self.denum = coprime(abs(top), abs(bottom))


    def __str__(self):
        if self.denum != 1:
            return (f'{self.num}/{self.denum}')
        else:
            return (f'{self.num}')
    def __repr__(self):
        return(f'Fraction({self.num},{self.denum})')

    def getNum(self):
        return int(self.num)
    def getDenum(self):
        return int(self.denum)

    def __truediv__(self, new_fraction):
        new_num = (self.num) * (new_fraction.denum)
        new_denum = (self.denum) * (new_fraction.num)
        return Fraction(new_num, new_denum)

    def __mul__(self, new_fraction):
        new_num = (self.num) * (new_fraction.num)
        new_denum = (self.denum) * (new_fraction.denum)
        return Fraction(new_num, new_denum)
    def __add__(self, new_fraction):
        new_num = (self.num) * (new_fraction.denum) + (new_fraction.num) * (self.denum)
        new_denum = (self.denum) * (new_fraction.denum)
        return Fraction(new_num, new_denum)
    def __iadd__(self, new_fraction):
        # allows you to use +=
        temp = self.__add__(new_fraction)
        self.num, self.denum = temp.num, temp.denum
        return self
    def __radd__(self, new_fraction):
        # reverse add order
        return new_fraction.__add__(self)
    def __sub__(self, new_fraction):
        new_num = (self.num) * (new_fraction.denum) - (new_fraction.num) * (self.denum)
        new_denum = (self.denum) * (new_fraction.denum)
        return Fraction(new_num, new_denum)

    def __eq__(self, new_fraction):
        return (self.num == new_fraction.num) and\
         (self.denum == new_fraction.denum)
    def __ne__(self, new_fraction):
        return not __eq__(new_fraction)
    def __gt__(self,new_fraction):
        temp = self.__sub__(new_fraction)
        return temp.getNum > 0
    def __ge__(self, new_fraction):
        return (self.__gt__(new_fraction)) or (self.__eq__(new_fraction))
    def __lt__(self, new_fraction):
        return new_fraction.__gt__(self)
    def __le__(self, new_fraction):
        return new_fraction.__ge__(self)


x = 1
x += 1
print(x)
a = Fraction(1,4)
print(repr(a))
print(a)

b = Fraction(-3,4)
a += b

print(a)
print(a + b)
print(a == b)
print(a)
c = Fraction(2,-4)
print(c)
