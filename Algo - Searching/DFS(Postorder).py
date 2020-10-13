def DFSPostorder(node,array):
    if node.left:
        DFSPostorder(node.left,array)
    if node.right:
        DFSPostorder(node.right,array)
    array.append(node.data)
    return array