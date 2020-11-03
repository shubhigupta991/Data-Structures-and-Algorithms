class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def push(self,value):
        self.data.append(value)
        self.length += 1

    def pop(self):
        deleted_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return deleted_item

    def peek(self):
        return self.data[self.length-1]

    def show(self):
        for i in range(self.length):
            print(self.data[self.length-1-i])

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
