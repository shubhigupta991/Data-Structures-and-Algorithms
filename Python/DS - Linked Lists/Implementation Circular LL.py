class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.next = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.length += 1

    def insert(self,data,index):
        new_node = Node(data)
        if index == 0:
            self.prepend(data)
        elif index >= self.length:
            self.append(data)
        else:
            temp = self.head
            for i in range(0,index):
                if i == index - 1:
                    new_node.next = temp.next
                    temp.next = new_node
                    break
                temp = temp.next
            self.length += 1

    def display(self):
        temp = self.head
        print(temp.data)
        temp = temp.next
        while temp != self.head:
            print(temp.data)
            temp = temp.next

    def remove(self,index):
        if index == 0:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            temp = self.head
            for i in range(0,index):
                if i == index - 1:
                    temp.next = temp.next.next
                    if index == self.length-1:
                        self.tail = temp
                temp = temp.next

    def search(self,data):
        index = 0
        temp = self.head
        while index < self.length:
            if temp.data == data:
                return index
            index += 1
            temp = temp.next
        else:
            return 'Element not found'

    def reverse(self):
        previous = None
        current = self.head

        following = current.next
        current.next = previous
        previous = current
        current = following

        while current != self.head:
            following = current.next
            current.next = previous
            previous = current
            current = following

        self.head.next = previous
        self.head = previous

my_list = CircularLinkedLists()
my_list.append(10)
my_list.append(5)
my_list.append(6)
my_list.prepend(1)
my_list.insert(99,2)
my_list.insert(23,34)
my_list.display()
my_list.remove(2)
print(my_list.search(99))
print(my_list.search(9))
my_list.display()
my_list.reverse()
my_list.display()