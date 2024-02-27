from typing import Optional
import random


class TreeNode:

  def __init__(self, value):
    self.value = value
    self.size = 1
    self.left: Optional['TreeNode'] = None
    self.right: Optional['TreeNode'] = None

  def get_random_node(self):
    index = random.randrange(0, self.size)
    print(index)
    return self.get_ith_node(index)

  def get_ith_node(self, i):
    left_size = self.left.size if self.left else 0
    print("self:", self.value, "index:", i, "left:",left_size)
    if self.left and i < left_size:
      print("go to left", i)
      return self.left.get_ith_node(i)
    elif i == left_size:
      print("found")
      return self
    elif self.right and i > left_size:
      index = i - (left_size + 1)
      print("go to right", index)
      return self.right.get_ith_node(index)

  def insert_in_order(self, value):
    if value <= self.value:
      if not self.left:
        self.left = TreeNode(value)
      else:
        self.left.insert_in_order(value)
    else:
      if not self.right:
        self.right = TreeNode(value)
      else:
        self.right.insert_in_order(value)
    self.size += 1

  def find(self, value):
    if self.value == value:
      return self
    elif value <= self.value:
      return self.left.find(value) if self.left else None
    elif value > self.value:
      return self.right.find(value) if self.right else None
    return None

  def print(self):
    print("value:", self.value, "size:", self.size)
    if self.left:
      self.left.print()
    if self.right:
      self.right.print()


tree = TreeNode(20)
tree.insert_in_order(10)
tree.insert_in_order(30)
tree.insert_in_order(5)
tree.insert_in_order(15)
tree.insert_in_order(3)
tree.insert_in_order(7)
tree.insert_in_order(17)

tree.print()

random_node = tree.get_random_node()
print(random_node.value if random_node else None)
