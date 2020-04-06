class LogicGate(object):
    def __init__(self, n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.perfromGateLogic()
        return self.output

class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pin = None
    def getPin(self):
        if self.pin == None:
            self.pin = int(input('Enter Pin input for the gate ' + \
            self.getLabel() + "-->"))
            return self.pin
        else:
            if isinstance(self.pin, int):
                return self.pin
            else:
                return self.pin.getFrom().getOutput()


    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        if self.pinA == None:
            self.pinA = int(input('Enter PinA input for the gate ' + \
            self.getLabel() + "-->"))
            return self.pinA
        else:
            if isinstance(self.pinA, int):
                return self.pinA
            else:
                return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            self.pinB = int(input('Enter PinB input for the gate ' + \
            self.getLabel() + "-->"))
            return self.pinB
        else:
            if isinstance(self.pinB, int):
                return self.pinB
            else:
                return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")



class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def perfromGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1) and (b == 1):
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
    def perfromGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1) or (b == 1):
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)
    def perfromGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

class NnotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)
    def perfromGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 1
        else:
            return 0


class NandGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def perfromGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1) and (b == 1):
            return 0
        else:
            return 1

class NorGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def perfromGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1) or (b == 1):
            return 0
        else:
            return 1

class XorGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def perfromGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a + b == 1:
            return 1
        else:
            return 0


class connector(object):
    def __init__(self, fGate, tGate):
        self.fromGate = fGate
        self.toGate = tGate

        tGate.setNextPin(self)

    def getFrom(self):
        return self.fromGate
    def getTo(self):
        return self.toGate

class halfAdder(object):
    def __init__(self,n):
        self.label = n
        self.pinA = NnotGate(f"{n}_pinA")
        self.pinB = NnotGate(f"{n}_pinB")
        self.sum = XorGate(f"{n}_sum")
        self.carry = AndGate(f"{n}_carry")
        self.c1 = connector(self.pinA, self.sum)
        self.c2 = connector(self.pinB, self.sum)
        self.c3 = connector(self.pinA, self.carry)
        self.c4 = connector(self.pinB, self.carry)


    def getSum(self):
        return self.sum.getOutput()
    def getCarry(self):
        return self.carry.getOutput()

class fullAdder(object):
    def __init__(self,n):
        self.half1 = halfAdder(f"{n}_half1")
        self.half2 = halfAdder(f"{n}_half2")
        self.or_gate = OrGate(f"{n}_or")
        self.c1 = connector(self.half2.sum ,self.half1.pinB)
        self.c2 = connector(self.half1.carry, self.or_gate)
        self.c3 = connector(self.half2.carry, self.or_gate)
    def getSum(self):
        return self.half1.getSum()
    def getCarry(self):
        return self.or_gate.getOutput()

class BinaryAdder(object):
    def __init__(self, n):
        self.add1 = halfAdder(f"{n}_add1")
        self.add2 = fullAdder(f"{n}_add2")
        self.add3 = fullAdder(f"{n}_add3")
        self.add4 = fullAdder(f"{n}_add4")
        self.add5 = fullAdder(f"{n}_add5")
        self.add6 = fullAdder(f"{n}_add6")
        self.add7 = fullAdder(f"{n}_add7")
        self.add8 = fullAdder(f"{n}_add8")
        self.c1 = connector(self.add1.carry, self.add2.half1.pinA)
        self.c2 = connector(self.add2.or_gate, self.add3.half1.pinA)
        self.c3 = connector(self.add3.or_gate, self.add4.half1.pinA)
        self.c4 = connector(self.add4.or_gate, self.add5.half1.pinA)
        self.c5 = connector(self.add5.or_gate, self.add6.half1.pinA)
        self.c6 = connector(self.add6.or_gate, self.add7.half1.pinA)
        self.c7 = connector(self.add7.or_gate, self.add8.half1.pinA)
    def getResult(self):
        result = ""
        result += str(self.add8.getSum())
        result += str(self.add7.getSum())
        result += str(self.add6.getSum())
        result += str(self.add5.getSum())
        result += str(self.add4.getSum())
        result += str(self.add3.getSum())
        result += str(self.add2.getSum())
        result += str(self.add1.getSum())

        return result

def BinToDec(binaryString):
    result = 0
    l = len(binaryString)
    for i in range(l):
        result += int(binaryString[l-i-1]) * (2**i)
    return result



#g1 = AndGate("G1")
#g2 = AndGate("G2")
#g3 = OrGate("G3")
#g4 = NotGate("G4")
#c1 = connector(g1, g3)
#c2 = connector(g2, g3)
#c3 = connector(g3, g4)
#a = g4.getOutput()
#print(a)

#f1 = fullAdder("F1")
#b = f1.getSum()
#c = f1.getCarry()
#print(b)
#print(c)

b1 = BinaryAdder('B1')
r = b1.getResult()
print(r)
dr = BinToDec(r)
print(dr)
