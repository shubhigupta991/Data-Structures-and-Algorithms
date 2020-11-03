class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if data < temp.data:
                    if temp.left == None:
                        temp.left = new_node
                        break
                    else:
                        temp = temp.left
                elif data > temp.data:
                    if temp.right == None:
                        temp.right = new_node
                        break
                    else:
                        temp = temp.right

    def lookup(self,data):
        temp = self.root
        while temp:
            if data == temp.data:
                return True
            elif data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def remove(self,value):
        '''For this i function i follwed the right subtree smallest node approach, the other approch can be left subtree largest nde approach
            These are the two approaches for deleting the node having two subtrees'''
        if self.root == None:
            return False
        else:
            current_node = self.root
            parent_node = None
            i = 0
            while current_node and current_node.data != value:
                if value < current_node.data:
                    parent_node = current_node
                    current_node = current_node.left

                elif value > current_node.data:
                    parent_node = current_node
                    current_node = current_node.right
            if  current_node == None:
                print(current_node)
                return 'nhi mila'
            if current_node.left and current_node.right:
                leftmost = current_node.right
                parent_leftmost = current_node
                while leftmost.left != None:
                    parent_leftmost = leftmost
                    leftmost = leftmost.left
                parent_leftmost.left = leftmost.right
                leftmost.left = current_node.left
                leftmost.right = current_node.right
                if parent_node == None:
                    self.root = leftmost
                else:
                    if current_node.data < parent_node.data:
                        parent_node.left = leftmost
                    else:
                        parent_node.right = leftmost
            elif current_node.left:
                if parent_node == None:
                    self.root = current_node.left
                else:
                    if current_node.data < parent_node.data:
                        parent_node.left = current_node.left
                    else:
                        parent_node.right  = current_node.left
            elif current_node.right:
                if parent_node == None:
                    self.root = current_node.left
                else:
                    if current_node.data < parent_node.data:
                        parent_node.left = current_node.right
                    else:
                        parent_node.right  = current_node.right
            else:
                if parent_node == None:
                    self.root = None
                else:
                    if current_node.data < parent_node.data:
                        parent_node.left = None
                    else:
                        parent_node.right  = None
        return True

my_BST = BST()
my_BST.insert(9)
my_BST.insert(4)
my_BST.insert(20)
my_BST.insert(1)
my_BST.insert(170)
my_BST.insert(6)
my_BST.insert(15)
my_BST.insert(3)
print(my_BST.lookup(170))
print(my_BST.lookup(0))
print(my_BST.remove(9))
print(my_BST.root.data)
