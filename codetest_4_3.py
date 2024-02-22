from linked_list import ListNode, LinkedList
from binary_tree import BinaryTree, TreeNode
from codetest_4_2 import create_min_height_bst

def create_level_linked_list(root):
  level_list = []
  create_level_linked_list_helper(root, level_list, 0)
  return level_list

def create_level_linked_list_helper(root, level_list, level):
  # if root is none, then return
  if not root:
    return
  
  linked_list = None
  # if this is first time this level is being visited,  create a new level linked list in the level_list
  if len(level_list)==level:
    linked_list = LinkedList()
    level_list.append(linked_list)
  else:
    # if the linked_list already exist in the level_list, just retrieve it and add the root to that level_list linked list
    linked_list = level_list[level]
  linked_list.append(root)
  create_level_linked_list_helper(root.left, level_list, level+1)
  create_level_linked_list_helper(root.right, level_list, level+1)


  