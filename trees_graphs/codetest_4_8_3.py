from .sample_btree_a import node_15, node_9, node_12

# to see if p and q are on the same substree.
# if they are, then move down and see which subtree cover p and q, until they diverge.
def common_ancestor(root, p, q):
  #handle if p or q not in the tree
  if not cover(root, p) or not cover(root, q):
    return None
  return ancestor_helper(root, p, q)


def cover(root, p):
  if not root:
    return False
  if root == p:
    return True
  return cover(root.left, p) or cover(root.right, p)


def ancestor_helper(root, p, q):
  # I don't quite understand when root would be None.
  if not root or root in (p, q):
    return root

  p_is_on_left = cover(root.left, p)
  q_is_on_left = cover(root.left, q)
  if p_is_on_left != q_is_on_left:
    return root
  child_side = root.left if p_is_on_left else root.right
  return ancestor_helper(child_side, p, q)


# node_15 is the root.
result = common_ancestor(node_15, node_9, node_12)
print(result)
