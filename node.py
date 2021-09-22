class Node:

    def __init__(self, nodeValue, rightChildValue = None, leftChildValue = None, parentValue = None):
        self.node = Node(nodeValue, rightChildValue, leftChildValue, self.parent)
        self.rightChild = Node(rightChildValue, self.node)
        self.leftChild = Node(leftChildValue, self.node)
        self.parent = Node(parentValue, self.parent.rightChild, self.parent.leftChild)

    def hasRightChild(self):
        return (True if self.rightChild else False)

    def hasLeftChild(self):
        return (True if self.leftChild else False)
