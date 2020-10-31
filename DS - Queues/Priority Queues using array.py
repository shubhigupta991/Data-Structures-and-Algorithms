class PriorityQueue():
    def __init__(self,maxsize=10):
        self.msize = maxsize
        self.data = [0 for _ in range(self.msize)]

    def push(self,value,priority):
        self.data[priority] = value

    def pop(self):
        deletedItem = self.data.pop(0)
        self.msize -= 1
        return deletedItem

    def peek(self):
        return self.data[0]

    def show(self):
        i = 0
        while i < self.msize and self.data[i] != 0:
            print(self.data[i])
            i += 1

myQueue = PriorityQueue(4)
myQueue.push(5,2)
myQueue.push(6,1)
myQueue.push(10,3)
myQueue.push(4,0)
myQueue.show()
print(myQueue.pop())
print(myQueue.peek())
myQueue.show()
