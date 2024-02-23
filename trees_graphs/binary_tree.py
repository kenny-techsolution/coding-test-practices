class TreeNode:

  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

  def __repr__(self):
    return str(self.value)

class BinaryTree:

  def __init__(self, root=None):
    self.root = root

  def print_tree(self, node, level=0, prefix="Root: "):
    if node is not None:
      print(" " * (level * 4) + prefix + str(node.value))
      if node.left or node.right:
        if node.left:
          self.print_tree(node.left, level + 1, "L--- ")
        else:
          print(" " * ((level + 1) * 4) + "L--- None")
        if node.right:
          self.print_tree(node.right, level + 1, "R--- ")
        else:
          print(" " * ((level + 1) * 4) + "R--- None")

  def visualize(self):
    self.print_tree(self.root)
