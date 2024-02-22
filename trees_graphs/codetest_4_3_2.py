from .linked_list import LinkedList
from .binary_tree import TreeNode, BinaryTree
from .codetest_4_2 import create_min_height_bst


def create_level_linked_list(root):
  level_list = []
  current_list = LinkedList()
  if root:
    current_list.append(root)
  count = 0
  # as long as current has stuff, that means we need to add it to the next level level list.
  while current_list.size():
    #add previous level
    count += 1
    print(count)
    level_list.append(current_list)
    # go to next level
    parents_list = current_list
    current_list = LinkedList()
    # the parents linked_list is used to go to build next level current.
    for parent in parents_list:
      if parent.left:
        current_list.append(parent.left)
      if parent.right:
        current_list.append(parent.right)
  return level_list


# test out with a binary tree
nums = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 14, 16, 40, 45]
tree = BinaryTree(create_min_height_bst(nums))
level_list = create_level_linked_list(tree.root)

for level, linked_list in enumerate(level_list):
  print(level)
  linked_list.print_list()
