class Node:

    def __init__(self, nodeValue, parentValue = None):
        self.value = nodeValue
        self.parent = parentValue
        self.rightChild = None
        self.leftChild = None

    def hasRightChild(self):
        return (True if self.rightChild else False)

    def hasLeftChild(self):
        return (True if self.leftChild else False)

    def hasBothChild(self):
        return (True if self.leftChild and self.rightChild else False)

    def toString(self):
        print(self.value)