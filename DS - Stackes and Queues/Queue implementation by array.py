class Queue:
    def __init__(self):
        self.data = []
        self.length = 0

    def enqueue(self,value):
        self.data.append(value)
        self.length += 1

    def dequeue(self):
        self.length -= 1
        return self.data.pop(0)


    def peek(self):
        return self.data[0]

    def show(self):
        for i in range(self.length):
            print(self.data[i])

myqueue = Queue()
myqueue.enqueue('google')
myqueue.enqueue('microsoft')
myqueue.enqueue('facebook')
myqueue.enqueue('apple')
myqueue.show()
myqueue.dequeue()
myqueue.show()
x = myqueue.peek()
print(x)