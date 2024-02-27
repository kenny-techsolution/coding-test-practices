from .sample_btree_d import node_15, node_8_b, node_8_c


def contain_tree(r1, r2):
  #traverse and create the array list for both r1 and r2.
  list_1 = []
  get_tree_as_list(r1, list_1)
  list_2 = []
  get_tree_as_list(r2, list_2)
  str1 = "".join(map(str, list_1))
  str2 = "".join(map(str, list_2))
  print(str1, str2)
  return str2 in str1


def get_tree_as_list(root, result):
  if not root:
    result.append("x")
    return
  result.append(root.value)
  get_tree_as_list(root.left, result)
  get_tree_as_list(root.right, result)
  return


is_b_subtree_of_a = contain_tree(node_15, node_8_b)
print(is_b_subtree_of_a)

is_c_subtree_of_a = contain_tree(node_15, node_8_c)
print(is_c_subtree_of_a)
