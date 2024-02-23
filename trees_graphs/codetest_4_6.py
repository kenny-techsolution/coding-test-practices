from .binary_tree import TreeNode


def in_order_successor(node):
  if not node:
    return None
  if node.right:
    return find_left_most_child(node.right)
  else:
    # if it's left child of the parent. then return parent.
    # if not, keep traverse up until hit a node which is a left child of a parent. return that parent.
    parent = node.parent
    child = node
    while parent and parent.left != child:
      child = parent
      parent = parent.parent
    return parent


def find_left_most_child(node):
  while node.left:
    node = node.left
  return node


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
node_13.parent = node_12

#test case 1
successor = in_order_successor(node_10)
print("10 next should be 11, answer:", successor.value)

#test case 2
successor = in_order_successor(node_11)
print("11 next should be 12, answer:", successor.value)

#test case 3
successor = in_order_successor(node_9)
print("9 next should be 10, answer:", successor.value)
