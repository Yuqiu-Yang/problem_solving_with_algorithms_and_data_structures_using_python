class jug:
    def __init__(self, max_volume, n):
        self.max_volume = max_volume
        self.volume = 0
        self.label = n
    def getVolume(self):
        return self.volume
    def getMaxVolume(self):
        return self.max_volume
    def isFull(self):
        return self.volume == self.max_volume
    def isEmpty(self):
        return self.volume == 0
    def addVolume(self, v):
        self.volume += v
    def empty_jug_to_group(self):
        print(f"Empty jug {self.label} to groud")
        self.volume = 0
    def fill_jug_with_tap_water(self):
        print(f"Fill jug {self.label} with tap water")
        self.volume = self.max_volume
    def pour_into_jug(self, other_jug):
        print(f"Pour water from jug {self.label} to jug {other_jug.label}")
        o_volume = other_jug.getVolume()
        o_mvolume = other_jug.getMaxVolume()
        temp = o_mvolume - o_volume
        other_jug.addVolume(min([temp, self.volume]))
        self.volume = max([0, self.volume - temp])



def jugsBrutal(L, S, R):
    pass




def jugsEuclidean(L, S, R):
    if (R <= 0) or (R > L + S):
        raise ValueError("Improper or boring R value")
    gcd ,x, y = euclidean(L, S)
    print(f"{x},{y}")
    if R % gcd != 0:
        raise ValueError("Can not be solved")
    else:
        temp = R//gcd
        x *= temp
        y *= temp
        Ljug = jug(L, "L")
        Sjug = jug(S, "S")
        if (x > 0) and (y > 0):
            Ljug.fill_jug_with_tap_water()
            Sjug.fill_jug_with_tap_water()
            print(f"Done! Jug {Ljug.label} has {Ljug.getVolume()}\
                    Jug {Sjug.label} has {Sjug.getVolume()}")
        elif (x == 0) and (y > 0):
            Sjug.fill_jug_with_tap_water()
        elif (x > 0) and (y == 0):
            Ljug.fill_jug_with_tap_water()
        else:
            if (x > 0):
                jugProcedure(Ljug, Sjug, x, y)
            else:
                jugProcedure(Sjug, Ljug, y, x)


def euclidean(a, b):
    if b == 0:
        return a, 1 , 0
    else:
        gcd, x, y = euclidean(b, a % b)
        return gcd, y, x - (a//b) * y


def jugProcedure(startJug, endJug, x, y):
    i = 0
    j = 0
    while True:
        if (i == x) and (j == y):
            break
        if startJug.isEmpty() and (i != x):
            startJug.fill_jug_with_tap_water()
            i += 1
            print(i)
        startJug.pour_into_jug(endJug)
        if endJug.isFull() and (j != y):
            endJug.empty_jug_to_group()
            j -= 1
            print(j)
    print(f"The volume in {startJug.label} is {startJug.getVolume()}\n \
            The volume in {endJug.label} is {endJug.getVolume()}")

#gcd, x, y = euclidean(5,3)

#Ljug = jug(5, "L")
#Sjug = jug(3, "S")
#jugProcedure()
#jugsEuclidean(21,9,3)
