from typing import Optional
import random


class TreeNode:
  def __init__(self, value):
    self.value = value
    self.size = 1
    self.left: Optional['TreeNode'] = None
    self.right: Optional['TreeNode'] = None

  def get_random_node(self):
    # see how many nodes on the left subtree. 
    left_size = self.left.size if self.left else 0
    # pick a random number from 0 to size of the current node
    size = self.size if self.size else 0
    # use randrange , sec param is exclusive. 
    index = random.randrange(0, self.size)
    print("random", index, left_size)
    # if the random number is less than size of the left size. it means the random should be on the left.
    if self.left and index < left_size:
      return self.left.get_random_node()
    # if the random index is equal to the size of the left subtree, then return the current node.
    elif index == left_size:
      return self
    # if the random index is more than left size, then get random number from the right subtee. 
    elif self.right and index > left_size:
      return self.right.get_random_node()
    return None
    
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
    self.size+=1

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

random = tree.get_random_node()
print(random.value if random else None)