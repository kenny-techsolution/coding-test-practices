from binary_tree import BinaryTree, TreeNode


def create_min_height_bst(nums: list):
  return min_height_bst_builder(nums, 0, len(nums) - 1)


def min_height_bst_builder(nums: list, start, end):
  print(nums[start], nums[end])
  if start > end:
    return None
  # find the middle index.
  # ex. [a]    -> 0/2 = 0        -> a
  # ex. [a, b] -> 1/2 = 0        -> a
  # ex. [a, b, c] -> 2/2 = 1     -> b
  # ex. [a, b, c, d] -> 3/2 = 1  -> b
  mid_index = (start + end) // 2
  print(nums[mid_index])
  # create a node for the mid
  root = TreeNode(nums[mid_index])
  # create the left and right child recursively
  root.left = min_height_bst_builder(nums, start, mid_index - 1)
  root.right = min_height_bst_builder(nums, mid_index + 1, end)
  return root


nums = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 14, 16, 40, 45]
tree = BinaryTree(create_min_height_bst(nums))
tree.visualize()
