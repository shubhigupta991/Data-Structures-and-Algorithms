class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.rear = None
        self.length = 0

    def enqueue(self,data):
        new_node = Node(data)
        if self.first == None:
            self.first = new_node
            self.rear = self.first

        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.first == None:
            return -1
        else:
            deletedItem = self.first.data
            self.first = self.first.next
            self.length -= 1
            return deletedItem

    def peek(self):
        if self.first == None:
            return -1
        return self.first.data

    def show(self):
        temp = self.first
        while temp:
            print(temp.data)
            temp = temp.next

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
