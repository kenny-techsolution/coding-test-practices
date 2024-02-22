from test_util import run_tests
from typing import Optional
from linked_list_class import ListNode, PartialSum, create_linked_list_from_list, insert_before, pad_list


def palindrome(linked_list) -> bool:
  # create a list that is of reversed order
  reversed_list = None
  current = linked_list
  while current:
    temp = reversed_list
    reversed_list = ListNode(current.value)
    reversed_list.next = temp
    current = current.next

  while linked_list and reversed_list:
    if linked_list.value != reversed_list.value:
      return False
    linked_list = linked_list.next
    reversed_list = reversed_list.next
  return True


linked_list_a: ListNode = create_linked_list_from_list(
    [1, 2, 5, 3, 8, 3, 5, 2, 1])

test_cases = [
    ((linked_list_a, ), True),
]

run_tests(palindrome, test_cases)
