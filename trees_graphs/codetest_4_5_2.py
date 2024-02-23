from .binary_tree import TreeNode, BinaryTree
from .codetest_4_2 import create_min_height_bst


# approach 2 - max min approach
def validateBST(root):

  def validateBSTHelper(root, min, max):
    if not root:
      return True
    if (min and min >= root.value) or (max and root.value > max):
      return False

    if (not validateBSTHelper(root.left, min, root.value)
        or not validateBSTHelper(root.right, root.value, max)):
      return False
    return True

  return validateBSTHelper(root, None, None)


nums = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 14, 16, 40, 45]
tree = BinaryTree(create_min_height_bst(nums))
valid = validateBST(tree.root)
print(valid)
