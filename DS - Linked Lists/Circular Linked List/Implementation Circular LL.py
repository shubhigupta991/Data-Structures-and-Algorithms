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
            i = 0
            while temp:
                if i == index - 1:
                    new_node = temp.next
                    temp.next = new_node
                    break
                    temp = temp.next
                    i += 1
            self.length += 1

    def display(self):
        temp = self.head
        while temp.next != self.head:
            print(temp.data)
            temp = temp.next

    def remove(self,index):
        if index == 0:
            self.head = self.head.next
        else:
            i = 0
            temp = self.head
            while temp.next != self.head:
                if i == index - 1:
                    temp.next = temp.next.next
                    if index == self.length-1:
                        self.tail = temp

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