from test_util import run_tests
from typing import Optional
from linked_list_class import ListNode, PartialSum, create_linked_list_from_list, insert_before, pad_list


# Part 2 is that l1, l2 is in reversed order.
def add_list(l1: ListNode, l2: ListNode) -> list:
  # first pad the shorter list to make them same length
  l1_len = len(l1.to_list())
  l2_len = len(l2.to_list())

  difference = l1_len - l2_len
  if difference > 0:
    l2 = pad_list(l2, difference)
  elif difference < 0:
    l1 = pad_list(l1, abs(difference))
  
  # calculate the l1 and l2 sum
  partial_sum: PartialSum = add_list_helper(l1, l2)

  # get the carry from calling the add_lit again.
  if partial_sum.carry > 0:
    final_list = insert_before(partial_sum, partial_sum.carry)
    return final_list.to_list()
  else:
    return partial_sum.list_sum.to_list() if partial_sum.list_sum else []

def add_list_helper(l1: Optional[ListNode],
                    l2: Optional[ListNode]) -> PartialSum:
  if not l1 and not l2:
    return PartialSum()

  #add smaller digits recursively
  l1_next = l1.next if l1 else None
  l2_next = l2.next if l2 else None
  partial_sum: PartialSum = add_list_helper(l1_next, l2_next)

  #add the current digit
  l1_value = l1.value if l1 else 0
  l2_value = l2.value if l2 else 0
  value = l1_value + l2_value + partial_sum.carry
  full_result = insert_before(partial_sum.list_sum, value % 10)
  partial_sum.list_sum = full_result
  partial_sum.carry = 1 if value >= 10 else 0
  return partial_sum


# 917 + 3295 = 4212
linked_list_a: ListNode = create_linked_list_from_list([9, 1, 7])
linked_list_b: ListNode = create_linked_list_from_list([3, 2, 9, 5])

linked_list_c: ListNode = create_linked_list_from_list([4, 2, 1, 2])

test_cases = [
    ((linked_list_a, linked_list_b), linked_list_c.to_list()),
]

run_tests(add_list, test_cases)
