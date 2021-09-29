from node import Node
from tree import Tree


nodeRoot = Node('A')
tree = Tree(nodeRoot)

nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')


tree.insertNode(nodeB, "L", nodeRoot)
tree.insertNode(nodeC, 'R', nodeRoot)
tree.insertNode(nodeD, 'L', nodeB)
tree.insertNode(nodeE, 'R', nodeB)
tree.insertNode(nodeF, 'L', nodeC)


#tree.erd(nodeRoot)
tree.toString(nodeRoot)