def DFSPreorder(node,array):
    array.append(node.data)
    if node.left:
        DFSPreorder(node.left,array)
    if node.right:
        DFSPreorder(node.right,array)
    return array