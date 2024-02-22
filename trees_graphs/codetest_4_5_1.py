from .linked_list import LinkedList
from .binary_tree import TreeNode, BinaryTree
from .codetest_4_2 import create_min_height_bst


# approach 1 - recursive checking - in order traversal.
def validateBST(root):
  last_node = None

  def validate_helper(root):
    nonlocal last_node
    #handle base case
    if not root:
      return True

    # check / recurse left
    if not validate_helper(root.left):
      return False

    # check current
    print(root.value)
    print("last", last_node)
    if last_node and root.value <= last_node.value:
      return False
    last_node = root

    # check / recurse right
    if not validate_helper(root.right):
      return False

    # all good.
    return True

  return validate_helper(root)


nums = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 14, 16, 40, 45]
tree = BinaryTree(create_min_height_bst(nums))
valid = validateBST(tree.root)
print(valid)
