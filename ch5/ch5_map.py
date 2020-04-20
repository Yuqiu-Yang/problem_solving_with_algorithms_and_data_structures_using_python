from copy import deepcopy

class HashTable:
    def __init__(self, tableSize, hashMethod = "None", rehashMethod = "Linear_1"):
        self.size = tableSize
        self.slots = [[] for x in range(self.size)]
        self.data = [[] for x in range(self.size)]
        self.hashMethod = hashMethod
        self.rehashMethod = rehashMethod
    def increaseSize(self):
        self.size *= 2
        temp_slots = deepcopy(self.slots)
        temp_data = deepcopy(self.data)
        self.slots = [[] for x in range(self.size)]
        self.data = [[] for x in range(self.size)]
        for i in range(len(temp_slots)):
            for j in range(len(temp_slots[i])):
                key = temp_slots[i][j]
                data = temp_data[i][j]
                hashValue = self.hashFunction(key)
                if len(self.slots[hashValue]) == 0:
                    # if it happens to be an empty slot,
                    # we insert the key, data pair
                    self.slots[hashValue].append(key)
                    self.data[hashValue].append(data)
                else:
                    if key in self.slots[hashValue]:
                        # if the key is present
                        # we replace the data
                        temp_ind = self.slots[hashValue].index(key)
                        self.data[hashValue][temp_ind] = data
                    else:
                        # if a collision happens
                        if self.rehashMethod == "Chaining":
                            # if we are using Chaining as our
                            # rehashing method, we simply
                            # append the key and the data
                            self.slots[hashValue].append(key)
                            self.data[hashValue].append(data)
                        else:
                            # if we are using open addressing
                            # we need to find the next empty slot
                            rehashTime = 1
                            nextSlot = self.rehash(hashValue, rehashTime)
                            while (len(self.slots[nextSlot]) != 0) and \
                                not (key in self.slots[nextSlot]):
                                rehashTime += 1
                                nextSlot = self.rehash(nextSlot, rehashTime)
                            if len(self.slots[nextSlot]) == 0:
                                self.slots[nextSlot].append(key)
                                self.data[nextSlot].append(data)
                            else:
                                temp_ind = self.slots[nextSlot].index(key)
                                self.data[nextSlot][temp_ind] = data

    def put(self, key, data):
        lam = self.getLoadingFactor()
        if lam > 0.95:
            self.increaseSize()
        hashValue = self.hashFunction(key)
        if len(self.slots[hashValue]) == 0:
            # if it happens to be an empty slot,
            # we insert the key, data pair
            self.slots[hashValue].append(key)
            self.data[hashValue].append(data)
        else:
            if key in self.slots[hashValue]:
                # if the key is present
                # we replace the data
                temp_ind = self.slots[hashValue].index(key)
                self.data[hashValue][temp_ind] = data
            else:
                # if a collision happens
                if self.rehashMethod == "Chaining":
                    # if we are using Chaining as our
                    # rehashing method, we simply
                    # append the key and the data
                    self.slots[hashValue].append(key)
                    self.data[hashValue].append(data)
                else:
                    # if we are using open addressing
                    # we need to find the next empty slot
                    rehashTime = 1
                    nextSlot = self.rehash(hashValue, rehashTime)
                    while (len(self.slots[nextSlot]) != 0) and \
                        not (key in self.slots[nextSlot]):
                        rehashTime += 1
                        nextSlot = self.rehash(nextSlot, rehashTime)
                    if len(self.slots[nextSlot]) == 0:
                        self.slots[nextSlot].append(key)
                        self.data[nextSlot].append(data)
                    else:
                        temp_ind = self.slots[nextSlot].index(key)
                        self.data[nextSlot][temp_ind] = data
    def get(self, key):
        hashValue = self.hashFunction(key)
        data = None
        if self.rehashMethod == "Chaining":
            # if we are using Chaining then we only need to
            # check if the key is present in the list
            if key in self.slots[hashValue]:
                temp_ind = self.slots[hashValue].index(key)
                data = self.data[nextSlot][temp_ind]
        else:
            stop = False
            found = False
            position = hashValue
            rehashTime = 1
            while (len(self.slots[position]) != 0) and \
                    not found and not stop:
                if (key in self.slots[position]):
                    found = True
                    data = self.data[position][0]
                else:
                    position = self.rehash(position, rehashTime)
                    rehashTime += 1
                    if position == hashValue:
                        stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key, data)
    def len(self):
        sum = 0
        for i in range(len(self.slots)):
            sum += len(self.slots[i])
        return sum
    def __len__(self):
        return self.len()
    def __contains__(self, key):
        if self.get(key) == None:
            return False
        else:
            return True
    def __delitem__(self, key):
        hashValue = self.hashFunction(key)
        if self.rehashMethod == "Chaining":
            if key in self.slots[hashValue]:
                temp_ind = self.slots[hashValue].index(key)
                self.slots[hashValue].pop(temp_ind)
                self.data[hashValue].pop(temp_ind)
            else:
                raise ValueError(f"{key} is not in the table")
        else:
            found = False
            stop = False
            position = hashValue
            rehashTime = 1
            while (len(self.slots[position]) != 0) and \
                not found and not stop:
                if (key in self.slots[position]):
                    found = True
                else:
                    position = self.rehash(position, rehashTime)
                    rehashTime += 1
                    if position == hashValue:
                        stop = True
                        raise ValueError(f"{key} is not in the table")
            if found:
                self.slots[position].pop()
                self.data[position].pop()
            else:
                raise ValueError(f"{key} is not in the table")
    def getLoadingFactor(self):
        return (self.len())/(self.size)
    def getSearchingSteps(self):
        lam = self.getLoadingFactor()
        if self.rehashMethod == "Chaining":
            return (1 + lam / 2, lam)
        else:
            return (0.5 * (1 + 1/(1 - lam)), 0.5 * (1 + 1/((1 - lam)**2)))
    def hashFunction(self, key):
        if self.hashMethod == "Folding":
            # group of 2
            key_str = str(key)
            pos = 0
            sum = 0
            while pos < len(key_str):
                sum += int(key_str[pos:(pos + 2)])
                pos += 2
            return sum%(self.size)
        elif self.hashMethod == "RevFolding":
            # group of 2
            # and reverse every other group
            key_str = str(key)
            pos = 0
            sum = 0
            count = 0
            while pos < len(key_str):
                if count % 2 == 0:
                    sum += int(key_str[pos:(pos + 2)])
                else:
                    sum += int(key_str[(pos+1):(pos-1):-1])
                pos += 2
                count += 1
            return sum%(self.size)
        elif self.hashMethod == "MidSquare":
            # the middle 2
            key_str = str(int(key) ** 2)
            midPt = len(key_str)//2
            key_int = int(key_str[max([0, (midPt - 1)]):(midPt + 1)])
            return (key_int)%(self.size)
        else:
            return int(key)%(self.size)
    def rehash(self, oldHash, rehashTime = 1):
        if self.rehashMethod == "Quadratic":
            return (oldHash + (rehashTime**2))%self.size
        elif self.rehashMethod == "Chaining":
            return oldHash
        else:
            step_size = int(self.rehashMethod.split("_")[1])
            return (oldHash + step_size)%self.size
