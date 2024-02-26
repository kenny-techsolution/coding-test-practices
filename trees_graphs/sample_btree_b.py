from .binary_tree import TreeNode
from .binary_tree import BinaryTree


node_50 = TreeNode(50)
node_20 = TreeNode(20)
node_60 = TreeNode(60)
node_10 = TreeNode(10)
node_25 = TreeNode(25)
node_70 = TreeNode(70)

node_50.left = node_20
node_50.right = node_60
node_20.left = node_10
node_20.right = node_25
node_60.right = node_70

tree = BinaryTree(node_50)
tree.visualize()
