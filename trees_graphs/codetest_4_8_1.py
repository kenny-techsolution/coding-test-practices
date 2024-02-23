from .sample_btree_a import node_9, node_12

# node with link to parent, method 1.
def common_ancestor(p, q):
  depth_diff = depth(p) - depth(q)
  # see which is the shallower node. 
  shallow_node = q if depth_diff > 0 else p
  deeper_node = p if depth_diff > 0 else q
  deeper_node = go_up_by(deeper_node, abs(depth_diff))

  # find where paths intersect
  while (shallow_node != deeper_node and shallow_node and deeper_node):
    shallow_node = shallow_node.parent
    deeper_node = deeper_node.parent
  return None if (not shallow_node) or (not deeper_node) else shallow_node

def depth(node):
  depth = 0
  while node.parent:
    node = node.parent
    depth+=1
  return depth

def go_up_by(node, depth):
  while depth:
    node = node.parent
    depth-=1
  return node


result = common_ancestor(node_9, node_12)
print(result)
