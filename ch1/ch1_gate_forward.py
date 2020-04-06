class pin(object):
    def __init__(self, n):
        self.label = n
        self.value = 0
    def getLabel(self):
        return self.label
    def getValue(self):
        return self.value
    def setValue(self, sig):
        self.value = sig

class connector(object):
    def __init__(self, fGate, tGate, pinNum):
        self.fromGate = fGate
        self.toGate = tGate
        self.fromPin = self.fromGate.getOutputPin()
        self.toPin = self.toGate.getInputPin(pinNum)

        self.toPin.setValue(self.fromPin.getValue())
        if self.fromGate.getPower():
            self.toGate.powerOn()

class LogicGate(object):
    def __init__(self, n):
        self.label = n
        self.power = False
        self.outputPin = pin(f"{n}_output")
    def getLabel(self):
        return self.label
    def getPower(self):
        return self.power
    def getOutputPin(self):
        return self.outputPin

class UnaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)
        self.inputPin1 = pin(f"{n}_input1")
    def getInputPin(self,num):
        return self.inputPin1

class NotGate(UnaryGate):
    def __init__(self,n):
        super().__init__(n)
    def powerOn(self):
        self.power = True
        if self.getInputPin(1).getValue() == 1:
            self.getOutputPin().setValue(0)
        else:
            self.getOutputPin().setValue(1)


class BinaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)
        self.inputPin1 = pin(f"{n}_input1")
        self.inputPin2 = pin(f"{n}_input2")
    def getInputPin(self,num):
        if num == 1:
            return self.inputPin1
        else:
            return self.inputPin2

class AndGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def powerOn(self):
        self.power = True
        if (self.inputPin1.getValue() == 1) and\
         (self.inputPin2.getValue() == 1):
            self.outputPin.setValue(1)
        else:
            self.outputPin.setValue(0)

class OrGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def powerOn(self):
        self.power = True
        if (self.inputPin1.getValue() == 1) or\
         (self.inputPin2.getValue() == 1):
            self.outputPin.setValue(1)
        else:
            self.outputPin.setValue(0)



g1 = AndGate("G1")
g1.getInputPin(1).setValue(1)
g1.getInputPin(2).setValue(0)
g1.powerOn()

g2 = AndGate("G2")
g2.getInputPin(1).setValue(1)
g2.getInputPin(2).setValue(0)
g2.powerOn()

g3 = OrGate("G3")

g4 = NotGate("G4")

c1 = connector(g1, g3, 1)
c2 = connector(g2, g3, 2)
c3 = connector(g3, g4, 1)
