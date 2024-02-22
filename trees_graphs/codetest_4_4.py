from .linked_list import LinkedList
from .binary_tree import TreeNode, BinaryTree


def is_tree_balance(root):
  return check_height(root) != -float('inf')


def check_height(root):
  #if the root is None
  if not root:
    return -1
  #check left subtree height:
  left_height = check_height(root.left)
  if left_height == -float('inf'):
    return -float('inf')
  right_height = check_height(root.right)
  if right_height == -float('inf'):
    return -float('inf')
  height_diff = abs(right_height - left_height)
  if height_diff > 1:
    return -float('inf')
  else:
    return 1 + max(left_height, right_height)


node_a = TreeNode('a')
node_b = TreeNode('b')
node_c = TreeNode('c')
node_d = TreeNode('d')
node_e = TreeNode('e')
node_f = TreeNode('f')
node_g = TreeNode('g')

node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

balance = is_tree_balance(node_a)
print(balance)

node_a.left = node_b
node_a.right = node_f
node_b.left = node_c
node_c.left = node_d
node_d.left = node_e

balance = is_tree_balance(node_a)
print(balance)
