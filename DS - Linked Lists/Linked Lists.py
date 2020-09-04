class Node:
    def __init__(self,data):
        self.data = data
        self.ptr = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.ptr = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.ptr = self.head
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
            for i in range(0,self.length):
                if i == index-1:
                    new_node.ptr = temp.ptr
                    temp.ptr = new_node
                    break
                temp = temp.ptr
            self.length += 1

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.ptr

    def remove(self,index):
        temp = self.head
        if index == 0:
            self.head = self.head.ptr
        else:
            for i in range(self.length):
                if i == index-1:
                    temp.ptr = temp.ptr.ptr
                    break
                temp = temp.ptr
        self.length -= 1

    def search(self,value):
        temp = self.head
        index = 0
        while temp != None:
            if temp.data == value:
                return index
            index += 1
            temp = temp.ptr
        else:
            return 'Element not found'

    def reverse(self):
        previous = None
        current = self.head
        following = current.ptr
        while current:
            current.ptr = previous
            previous = current
            current = following
            if following:
                following = following.ptr
        self.head = previous

my_list = LinkedList()
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