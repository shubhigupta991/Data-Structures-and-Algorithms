'''
A heap tree is implemented mostly using arrays, Where the node is stored at i and its left child is at 2*i and
its right child is at 2*i+1(if the indexing is done from 1
else left child at 2*i+1 right child at 2*i+2 if indexing is done from 0).

Also Heap trees are of two types:
Max Heap
Min Heap

Here I am implementing Max heap
'''
class Heap():
    '''
    This class creates heap from the values given individually.
    '''
    def __init__(self):
        self.data = []
        self.currentLength = 0

    def insert(self,value):
        '''
        To add value in a heap.
        :param value: the data that's need to be inserted
        :return: None (as it is an inplace insertion)
        '''
        self.data.append(value)
        self.currentLength += 1
        currentNode = self.currentLength
        parentNode = currentNode // 2
        indexOfCurrentNode = currentNode - 1
        indexOfParentNode = parentNode - 1
        while self.data[indexOfCurrentNode] > self.data[indexOfParentNode]:
            self.data[indexOfParentNode],self.data[indexOfCurrentNode] = self.data[indexOfCurrentNode],self.data[indexOfParentNode]
            currentNode = parentNode
            parentNode = currentNode // 2
            indexOfCurrentNode = currentNode - 1
            indexOfParentNode = parentNode - 1
            if indexOfCurrentNode == 0:
                return

    def delete(self):
        '''
        In a heap the only node that can be deleted is the root node.
        :return: deletedItem
        '''
        deletedElement = self.data[0]
        self.data[0] = self.data[self.currentLength - 1]
        del self.data[self.currentLength - 1]
        self.currentLength -=1
        currentNode = 1
        leftChild = 2 * currentNode
        rightChild = 2 * currentNode + 1
        indexOfCurrentNode = 0
        indexOfLeftChild = leftChild - 1
        indexOfRightChild = rightChild - 1
        while self.data[indexOfCurrentNode] < self.data[indexOfLeftChild] or self.data[indexOfCurrentNode] < self.data[indexOfRightChild] :
            if self.data[indexOfLeftChild] > self.data[indexOfRightChild]:
                self.data[indexOfCurrentNode],self.data[indexOfLeftChild] = self.data[indexOfLeftChild],self.data[indexOfCurrentNode]
                currentNode = leftChild
                leftChild = 2 * currentNode
                rightChild = 2 * currentNode + 1
                indexOfCurrentNode = currentNode - 1
                indexOfLeftChild = leftChild - 1
                indexOfRightChild = rightChild - 1
            elif self.data[indexOfLeftChild] < self.data[indexOfRightChild]:
                self.data[indexOfCurrentNode],self.data[indexOfLeftChild] = self.data[indexOfLeftChild],self.data[indexOfCurrentNode]
                currentNode = rightChild
                leftChild = 2 * currentNode
                rightChild = 2 * currentNode + 1
                indexOfCurrentNode = currentNode - 1
                indexOfLeftChild = leftChild - 1
                indexOfRightChild = rightChild - 1
            if currentNode >= self.currentLength or leftChild >= self.currentLength or rightChild >= self.currentLength:
                return deletedElement

class Heap2:
    '''
    This class helps create heap when given array of values
    '''
    def __init__(self,array):
        '''
        constructor to create desired heap
        :param array: set of values to create heap.
        '''
        self.data = array
        for i in range(1, len(array)):
            currentNode = i+1
            parentNode = currentNode // 2
            indexOfCurrentNode = currentNode - 1
            indexOfParentNode = parentNode - 1
            while self.data[indexOfCurrentNode] > self.data[indexOfParentNode]:
                self.data[indexOfParentNode], self.data[indexOfCurrentNode] = self.data[indexOfCurrentNode], self.data[indexOfParentNode]
                currentNode = parentNode
                parentNode = currentNode // 2
                indexOfCurrentNode = currentNode - 1
                indexOfParentNode = parentNode - 1
                if indexOfCurrentNode == 0:
                    return


myHeap = Heap()
myHeap.insert(30)
myHeap.insert(20)
myHeap.insert(15)
myHeap.insert(5)
myHeap.insert(10)
myHeap.insert(12)
myHeap.insert(6)
print(myHeap.data)
myHeap.insert(40)
print(myHeap.data)
myHeap.insert(35)
print(myHeap.data)
myHeap.insert(50)
print(myHeap.data)
print("Deleted Element : ",myHeap.delete())
print(myHeap.data)
print(myHeap.currentLength)
myHeap2 = 