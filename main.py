from node import Node
from binaryTree import BinaryTree


nodeRoot = Node(6)
binaryTree = BinaryTree(nodeRoot)

nodeB = Node(2)
nodeC = Node(5)
nodeD = Node(8)
nodeE = Node(1)
nodeF = Node(29)


binaryTree.insertNode(nodeB, 'L', nodeRoot)
binaryTree.insertNode(nodeC, 'R', nodeRoot)
binaryTree.insertNode(nodeD, 'L', nodeB)
binaryTree.insertNode(nodeE, 'R', nodeB)
binaryTree.insertNode(nodeF, 'L', nodeC)

binaryTree.navigation('LNR', nodeRoot)


#tree.erd(nodeRoot)
#tree.toString(nodeRoot)