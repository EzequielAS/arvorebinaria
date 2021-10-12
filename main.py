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

print('Left-Right-Node')
print(' ')
binaryTree.navigation('LRN', nodeRoot)
print(' ')

print('Left-Node-Right')
print(' ')
binaryTree.navigation('LNR', nodeRoot)
print(' ')

print('Node-Left-Right')
print(' ')
binaryTree.navigation('NLR', nodeRoot)
print(' ')

print('Árvore Binária')
print(' ')
binaryTree.printTree(nodeRoot)
print(' ')

print('Árvore Binária de Busca')
print(' ')
binaryTree.transformBinaryTreeIntoBinarySearchTree(binaryTree.nodeRoot)
