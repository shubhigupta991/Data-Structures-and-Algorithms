class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self,index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length +=1

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem

    def delete(self,index):
        deletedItem = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -=1
        return deletedItem

arr = MyArray()
arr.push('Hello')
arr.push('Everyone')
arr.push('!')
arr.pop()
arr.get(1)
arr.delete(0)
print(arr)

