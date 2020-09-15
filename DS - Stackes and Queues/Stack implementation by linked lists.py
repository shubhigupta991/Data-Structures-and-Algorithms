class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self,data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length +=1

    def pop(self):
        if self.top == None:
            return None
        deleted_data = self.top.data
        self.top = self.top.next
        self.length -= 1
        if self.length == 0:
            self.bottom = None
        return deleted_data

    def peek(self):
        return self.top.data

    def show(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next

mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
mystack.show()
x = mystack.peek()
print(x)
y=mystack.pop()
print(y)
qw = mystack.peek()
print(qw)
mystack.show()
