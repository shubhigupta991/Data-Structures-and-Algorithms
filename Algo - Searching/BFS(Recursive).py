''' This function represents recursive implementation of BFS'''
def BFSrecursive(queue, array):
    if len(queue) == 0:
        return array

    currentNode = queue.pop(0)
    array.append(currentNode.data)
    if currentNode.left:
        queue.append(currentNode.left)
    if currentNode.right:
        queue.append(currentNode.right)
    return BFSrecursive(queue, array)