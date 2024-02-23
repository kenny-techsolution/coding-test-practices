from .sample_btree_a import node_15, node_9, node_12


# node with link to parent, method 2.
def common_ancestor(root, p, q):
  # check either
  if not cover(root, p) or not cover(root, q):
    return None
  elif cover(p, q):
    return p
  elif cover(q, p):
    return q

  # traverse upward until you find a node that covers q.
  sibling = get_sibling(p)
  parent = p
  while not cover(sibling, q):
    sibling = get_sibling(parent)
    parent = parent.parent
  return parent


def get_sibling(p):
  if not p or not p.parent:
    return None
  parent = p.parent
  return parent.left if parent.right == p else parent.right


def cover(root, p):
  if not root:
    return False
  if root == p:
    return True
  return cover(root.left, p) or cover(root.right, p)

# node_15 is the root.
result = common_ancestor(node_15, node_9, node_12)
print(result)
