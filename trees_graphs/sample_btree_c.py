from .binary_tree import TreeNode
from .binary_tree import BinaryTree
"""
Root: 2
  L--- 3
  R--- 1
"""
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1 = TreeNode(1)

node_2.left = node_1
node_2.right = node_3

tree = BinaryTree(node_2)
tree.visualize()
