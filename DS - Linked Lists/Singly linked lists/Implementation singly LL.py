class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
        else:
            self.tail.next= new_node
            self.tail = new_node
        self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
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
                    new_node.next = temp.next
                    temp.next = new_node
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
            self.head = self.head.ptr
        else:
            for i in range(self.length):
                if i == index-1:
                    temp.next = temp.next.next
                    if index == self.length-1:
                        self.tail = temp
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
        previous = None
        current = self.head
        following = current.next
        while current:
            current.next = previous
            previous = current
            current = following
            if following:
                following = following.next
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