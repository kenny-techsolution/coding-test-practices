from .binary_tree import TreeNode
from .binary_tree import BinaryTree
# this tree is built based on the diagram I draw for 4.6 Successor quetsions's explanation in notion.
# tree a
"""
Root: 15
  L--- 10
      L--- 8
          L--- 7
          R--- 9
      R--- 12
          L--- 11
          R--- 13
  R--- 17
"""
node_15 = TreeNode(15)
node_10 = TreeNode(10)
node_17 = TreeNode(17)
node_8 = TreeNode(8)
node_12 = TreeNode(12)
node_7 = TreeNode(7)
node_9 = TreeNode(9)
node_12 = TreeNode(12)
node_11 = TreeNode(11)
node_13 = TreeNode(13)

node_15.left = node_10
node_15.right = node_17
node_10.left = node_8
node_10.right = node_12
node_10.parent = node_15
node_8.left = node_7
node_8.right = node_9
node_8.parent = node_10
node_7.parent = node_8
node_9.parent = node_8
node_12.left = node_11
node_12.right = node_13
node_12.parent = node_10
node_11.parent = node_12

tree = BinaryTree(node_15)
tree.visualize()

# tree b
# L--- 8
#   L--- 7
#   R--- 9

node_8_b = TreeNode(8)
node_7_b = TreeNode(7)
node_9_b = TreeNode(9)

node_8_b.left = node_7_b
node_8_b.right = node_9_b
node_7_b.parent = node_8_b
node_9_b.parent = node_8_b

# tree c
# L--- 8
#   L--- 7

node_8_c = TreeNode(8)
node_7_c = TreeNode(7)

node_8_c.left = node_7_c
node_7_c.parent = node_8_c


