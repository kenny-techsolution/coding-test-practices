from .binary_tree import TreeNode, BinaryTree
from .codetest_4_2 import create_min_height_bst

def in_order_traversal(root):
  if not root:
    return
  in_order_traversal(root.left)
  print(root.value)
  in_order_traversal(root.right)
  
def pre_order_traversal(root):
  if not root:
    return
  print(root.value)
  in_order_traversal(root.left)
  in_order_traversal(root.right)
  
def post_order_traversal(root):
  if not root:
    return
  in_order_traversal(root.left)
  in_order_traversal(root.right)
  print(root.value)

nums = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 14, 16, 40, 45]
tree = BinaryTree(create_min_height_bst(nums))

print("In order:")
in_order_traversal(tree.root)
print("Pre order:")
pre_order_traversal(tree.root)
print("Post order:")
post_order_traversal(tree.root)