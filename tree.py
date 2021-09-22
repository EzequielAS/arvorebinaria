from node import *

class Tree:

    def __init__(self, nodeRootValue, rightChildValue = None, leftChildValue = None):
        self.nodeRoot = Node(nodeRootValue, rightChildValue, leftChildValue)
        

    def insertNode(self, nodeValue, side, parent = Node, rightChild = None, leftChild = None):
        if side == 'R':
            parent.rightNode = Node(nodeValue, parent, rightChild, leftChild) 
        elif(side == 'L'):
            parent.leftNode =  Node(nodeValue, parent, rightChild, leftChild)



tree = Tree('raiz', 'noA', 'noB')
tree.insertNode('noA', 'R', tree.nodeRoot, '', 'noC')

print(tree.nodeRoot.node)
