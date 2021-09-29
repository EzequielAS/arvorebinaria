from node import *

class Tree:

    def __init__(self, nodeRoot):
        self.nodeRoot = nodeRoot
        

    def insertNode(self, node, side, parent):
        if side == "R":
            if parent.hasRightChild():
                print('ERROR - o nó já tem filho direito')
            else:
                node.parent = parent
                parent.rightChild = node
        elif side == 'L':
            if parent.hasLeftChild():
                print('ERROR - o nó pai já tem filho esquerdo')
            else:
                node.parent = parent
                parent.leftChild =  node

    def search(self, value, NodeInicio):
        if NodeInicio != None:
            if value == NodeInicio.name:
                return True
            self.search(NodeInicio.rightChild)
            self.search(NodeInicio.lefChild)
        else:
            return False

    def nodeDegree(self, node):
        degree = 0
        if node.hasRightChild():
            degree += 1
        if node.hasLeftChild():
            degree += 1
        return degree
    def nodeDepth(self, node):
        if self.isRoot(node): 
            return 0
        else:
            parent = node.parent
            return 1 + self.nodeDepth(parent)
    def nodeHeight(self, node):
        if node.hasChild() == False or node == None:
            return 0 
        else:
            hgLeft = self.nodeHeight(node.leftChild)
            hgRight = self.nodeHeight(node.rightChild)
            return (hgLeft + 1 if hgLeft > hgRight else hgRight + 1)

    def nodeLevel(self, node):
        return self.nodeDepth(node)

    def isRoot(self, node):
            return (True if node is self.nodeRoot else False)

    def erd(self, node):

        if(node != None):
            self.erd(node.leftChild)
            print("{0}".format(node.value))
            self.erd(node.rightChild)

    def toString(self, node):
        result = '  '
        if(node != None):
            if self.isRoot(node):
                print(node.value)
            if(node.hasLeftChild() == True):
                result += node.leftChild.value + ' '
                self.toString(node.leftChild)
            elif(node.hasRightChild() == True):
                result += node.rightChild.value + ''
                self.toString(node.rightChild) 
            print(result)
               
