from .binary_tree import TreeNode, BinaryTree
from collections import deque
from .sample_btree_b import node_50
from .sample_btree_c import node_2


def all_sequences(root: TreeNode):
  # recursive on the left substree
  # recursive on the right subtree
  result = []

  if not root:
    result.append(deque())
    return result

  prefix = deque()
  prefix.append(root.value)

  # recurse on left and right subtrees
  print("** top", root.value)
  left_seq = all_sequences(root.left)
  print("** left_seq", show_as_list(left_seq))
  right_seq = all_sequences(root.right)
  print("** right_seq", show_as_list(right_seq))

  # weave together each list from left and right subtrees
  for left in left_seq:
    for right in right_seq:
      # weaved is list of new deque(s) after weaving
      weaved = []

      weave_list(left, right, weaved, prefix)
      result += weaved

  print("result:", root.value, show_as_list(result))
  return result


def test_weave_list():
  # left = [deque([2, 1]), deque([1, 2])]
  # right = [deque([3, 4]), deque([4, 3])]
  left = deque([3, 2])
  right = deque([4, 5])
  weaved = []
  weave_list(left, right, weaved, deque([1]))
  print(weaved)

def weave_list(first_seq, second_seq, results, prefix):
  print("--" * len(list(prefix)), list(first_seq), list(second_seq),
        list(prefix))
  # if first or second seq is empty, clone prefix and add the remainder to the result.

  if not first_seq or not second_seq:
    result = deque(prefix)
    result.extend(first_seq)
    result.extend(second_seq)
    results.append(result)
    print("---" * len(list(prefix)), show_as_list(results))
    return

  # take first element from first sequence, append to prefix.
  # call weave_list, recursively.
  first = first_seq.popleft()
  prefix.append(first)
  weave_list(first_seq, second_seq, results, prefix)
  first_seq.appendleft(first)
  prefix.pop()

  # take first element from second sequence, append to prefix.
  # call weave_list, recursively.
  second = second_seq.popleft()
  prefix.append(second)
  weave_list(first_seq, second_seq, results, prefix)
  second_seq.appendleft(second)
  prefix.pop()


def show_as_list(results):
  new_result = []
  for i, item in enumerate(results):
    new_result.append(list(item))
  return new_result


# sequences = show_as_list(all_sequences(node_2))
# print(sequences)

test_weave_list()
