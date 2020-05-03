class ArrayList:
    def __init__(self):
        self.sizeExponent = 0
        self.maxSize = 0
        # lastIndex points at the index next to the last added item
        self.lastIndex = 0
        self.myArray = []
    def append(self, val):
        if self.lastIndex >= self.maxSize - 1:
            self.__resize()
        self.myArray[self.lastIndex] = val
        self.lastIndex += 1

    def __resize(self):
        newsize = 2 ** self.sizeExponent + 2
        print("newsize = ", newsize)
        newArray = [0] * newsize
        for i in range(self.maxSize):
            newArray[i] = self.myArray[i]
        self.maxSize = newsize
        self.myArray = newArray
        self.sizeExponent += 1
    def __getitem__(self, idx):
        if idx < self.lastIndex:
            return self.myArray[idx]
        else:
            raise LookupError('Index out of bounds')
    def __setitem__(self, idx, val):
        if idx < self.lastIndex:
            self.myArray[idx] = val
        else:
            raise LookupError('Index out of bounds')
    def insert(self, idx, val):
        if self.lastIndex >= self.maxSize - 1:
            self.__resize()
        for i in range(self.lastIndex - 1, idx - 1, -1):
            self.myArray[i + 1] = self.myArray[i]
        self.lastIndex += 1
        self.myArray[idx] = val
    def __delitem__(self, idx):
        for i in range(idx, self.lastIndex - 1):
            self.myArray[i] = self.myArray[i + 1]
        self.myArray[self.lastIndex - 1] = 0
        self.lastIndex -= 1
    def index(self, val):
        found = False
        idx = 0
        while (not found) and (idx < self.lastIndex):
            if self.myArray[idx] == val:
                found = True
            else:
                idx += 1
        if found:
            return idx
        else:
            return -1
    def pop(self, idx = -1):
        if idx < 0:
            result = self.myArray[self.lastIndex - 1]
            self.myArray[self.lastIndex - 1] = 0
            self.lastIndex -= 1
            return result
        else:
            result = self.myArray[idx]
            for i in range(idx, self.lastIndex - 1):
                self.myArray[i] = self.myArray[i + 1]
            self.myArray[self.lastIndex - 1] = 0
            self.lastIndex -= 1
            return result
    def __add__(self, array):
        newArrayList = ArrayList()
        for i in range(self.lastIndex):
            newArrayList.append(self.myArray[i])
        for i in range(array.lastIndex):
            newArrayList.append(array.myArray[i])
        return newArrayList
    def __mul__(self, n):
        newArrayList = ArrayList()
        for i in range(n):
            for j in range(self.lastIndex):
                newArrayList.append(self.myArray[j])
        return newArrayList

    def __iter__(self):
        return iter(self.myArray[0:(self.lastIndex - 1)])
