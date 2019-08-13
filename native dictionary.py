class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        result = 0
        for i in range(len(key)):
            result += (ord(key[i]) * (1+i))
        return result % self.size

    def is_key(self, key):
        slot_number = self.hash_fun(key)
        if self.slots[slot_number] == key:
            return True
        else:
            for i in range(self.size):
                slot_number += 1
                if slot_number == self.size:
                    slot_number = 0
                if self.slots[slot_number] == key:
                    return True
        return False

    def put(self, key, value):
        slot_number = self.hash_fun(key)
        if self.slots[slot_number] is None:
            self.slots[slot_number] = key
            self.values[slot_number] = value
        else:
            if self.slots[slot_number] == key:
                self.values[slot_number] = value 
            else:
                cont = True
                while cont == True:
                    slot_number += 1
                    if slot_number == self.size:
                        slot_number = 0
                    if self.slots[slot_number] == key:
                        self.values[slot_number] = value
                        cont = False
                    if self.slots[slot_number] is None:
                        self.slots[slot_number] = key
                        self.values[slot_number] = value
                        cont = False
                    if slot_number == self.hash_fun(key):
                        cont = False

    def get(self, key):
        slot_number = self.hash_fun(key)
        if self.slots[slot_number] == key:
            return self.values[slot_number]
        else:
            for i in range(self.size):
                slot_number += 1
                if slot_number == self.size:
                    slot_number = 0
                if self.slots[slot_number] == key:
                    return self.values[slot_number]
        return None
