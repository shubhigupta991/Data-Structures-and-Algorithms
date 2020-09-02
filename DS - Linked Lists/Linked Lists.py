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
            self.append(data)
        elif index >= self.length:
            self.prepend(data)
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

    '''def reverse(self):
        prev = None
        self.tail = self.head
        while self.head != None:
            temp = self.head
            self.head = self.head.ptr
            temp.ptr = prev
            prev = temp
        self.head = temp'''


my_list = LinkedList()
my_list.append(16)
my_list.prepend(10)
my_list.insert(5,1)
my_list.display()
my_list.reverse()

print(my_list.length)
print(my_list.head.data,my_list.tail.data)
