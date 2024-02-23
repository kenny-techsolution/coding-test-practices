from sample_btree_a import node_10, node_11, node_9


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


#test case 1
successor = in_order_successor(node_10)
print("10 next should be 11, answer:", successor.value)

#test case 2
successor = in_order_successor(node_11)
print("11 next should be 12, answer:", successor.value)

#test case 3
successor = in_order_successor(node_9)
print("9 next should be 10, answer:", successor.value)
