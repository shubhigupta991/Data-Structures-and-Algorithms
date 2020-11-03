class Node:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority
        self.next = None
class PriorityQueue:
    def __init__(self):
        self.head = None

    def push(self,value,priority):
        new_node = Node(value,priority)
        if self.head == None:
            self.head = new_node
        elif self.head.priority > priority:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None and temp.next.priority < priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    def pop(self):
        deletedItem = self.head.data
        self.head = self.head.next
        return deletedItem

    def peek(self):
        return self.head.data

    def show(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

myQueue = PriorityQueue()
myQueue.push(5,2)
myQueue.push(6,1)
myQueue.push(10,3)
myQueue.push(4,0)
myQueue.show()
print(myQueue.pop())
print(myQueue.peek())
myQueue.show()