def DFSInorder(node,array):
    if node.left:
        DFSInorder(node.left,array)
    array.insert(0,node.data)
    if node.right:
        DFSInorder(node.right,array)
    return array