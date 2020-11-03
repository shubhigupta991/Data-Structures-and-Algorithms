class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data):
        new_node = Node(data)
        temp = self.head
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1


    def insert(self, data, index):
        new_node = Node(data)
        temp = self.head
        if index == 0:
            self.prepend(data)
        elif index >= self.length:
            self.append(data)
        else:
            for i in range(0,index):
                if i == index-1:
                    leader = temp
                    follower = temp.next
                    new_node.prev = leader
                    new_node.next = follower
                    follower.prev = new_node
                    leader.next = new_node
                    break
                temp = temp.next
            self.length += 1

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def remove(self,index):
        temp = self.head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length -1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            for i in range(0,index):
                if i == index-1:
                    leader = temp
                    follower = temp.next.next
                    leader.next = follower
                    follower.prev = leader
                    break
                temp = temp.next
        self.length -= 1

    def search(self,value):
        temp = self.head
        index = 0
        while temp != None:
            if temp.data == value:
                return index
            index += 1
            temp = temp.next
        else:
            return 'Element not found'

    def reverse(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev

my_list = DoublyLinkedList()
my_list.append(10)
my_list.append(5)
my_list.append(6)
my_list.prepend(1)
my_list.insert(99,2)
my_list.insert(23,34)
my_list.remove(5)
print(my_list.search(99))
print(my_list.search(9))
my_list.display()
my_list.reverse()
my_list.display()