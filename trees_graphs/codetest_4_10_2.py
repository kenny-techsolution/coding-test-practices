from .sample_btree_d import node_15, node_8_b, node_8_c


def contain_tree(r1, r2):
  if not r2:
    return True
  return subtree(r1, r2)


def subtree(r1, r2):
  if not r1:
    return False
  elif r1.value == r2.value and match_tree(r1, r2):
    return True
  return subtree(r1.left, r2) or subtree(r1.right, r2)


def match_tree(r1, r2):
  if not r1 and not r2:
    return True
  elif not r1 or not r2:
    return False
  elif r1.value != r2.value:
    return False
  else:
    return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)


is_b_subtree_of_a = contain_tree(node_15, node_8_b)
print(is_b_subtree_of_a)

is_c_subtree_of_a = contain_tree(node_15, node_8_c)
print(is_c_subtree_of_a)
