class Hash:
    def __init__(self):
        self.size = 10
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def insert(self,key,value):
        index = self.hashing(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def get(self,key):
        index = self.hashing(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

    def hashing(self,key):
        sum = 0
        for n in range(len(key)):
            sum += ord(key[n])
        return sum % self.size

    def delete(self,key):
        index = self.hashing(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                del self.keys[index]
                del self.values[index]
            index = (index + 1) % self.size

if __name__ == "__main":
    Hash = Hash()
    #perform all the functions
    


