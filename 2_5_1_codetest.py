from test_util import run_tests
from typing import Optional
from linked_list_class import ListNode, create_linked_list_from_list


# use recursion
def add_list(l1: ListNode, l2: ListNode) -> list:
  # Initiates the recursive function to add two linked lists
  answer_list: Optional[ListNode] = add_list_recurse(l1, l2, 0)
  return answer_list.to_list() if answer_list else []

def add_list_recurse(l1: Optional[ListNode], l2: Optional[ListNode],
                     carry: int) -> Optional[ListNode]:
  # Recursively adds corresponding nodes of two linked lists
  if not l1 and not l2 and carry == 0:
    return None

  answer_list = None
  value = carry

  if l1:
    value += l1.value

  if l2:
    value += l2.value

  carry = 1 if value >= 10 else 0
  answer_value = value % 10

  # Create a new node for this sum
  answer_list = ListNode(answer_value)
  if l1 or l2:
    next_l1 = l1.next if l1 else None
    next_l2 = l2.next if l2 else None
    answer_list.next = add_list_recurse(next_l1, next_l2, carry)
  return answer_list



# 917 + 3295 = 4212
linked_list_a: ListNode = create_linked_list_from_list([7, 1, 9])
linked_list_b: ListNode = create_linked_list_from_list([5, 9, 2, 3])

linked_list_c: ListNode = create_linked_list_from_list([2, 1, 2, 4])

test_cases = [
    ((linked_list_a, linked_list_b), linked_list_c.to_list()),
]

run_tests(add_list, test_cases)
