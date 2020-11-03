''' All the functions are implemented keeping in mind the case
    of collisons which occur while storing data in hash tables.
    We can test them by craeting a hashtable with small size'''
class Hashtable:
    def __init__(self,size):
        self.size = size
        self.data = [[] for i in range(self.size)]

    def hash(self,key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size
        return hash

    def set(self,key,value):
        address = self.hash(key)
        self.data[address].append([key,value])
        return None

    def get(self,key):
        address = self.hash(key)
        reference = self.data[address]
        for element in reference:
            if element[0] == key:
                return element[1]
        return -1

    def remove(self,key):
        address = self.hash(key)
        reference = self.data[address]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return None
        return None

    def keys(self):
        keysArray = []
        for element in self.data:
            if element:
                if len(element) > 1:
                    for i in range(len(element)):
                        keysArray.append(element[i][0])
                else:
                    keysArray.append(element[0][0])
        return keysArray

myHashtable = Hashtable(50)
myHashtable.set('grapes',1000)
myHashtable.set('apples',400)
myHashtable.set('orange',6000)
myHashtable.set('mangoes',20000)
print(myHashtable.get('apples'))
print(myHashtable.get('banana'))
myHashtable.remove('apples')
print(myHashtable.keys())