from test_util import run_tests
from typing import Optional
from linked_list_class import ListNode, create_linked_list_from_list


def partition(linked_list, k):
  current = linked_list

  # iterate through the list, seperate the values into before and after list, then link two list together.
  before_list = None
  after_list = None
  before_head = None
  after_head = None
  while current:
    if current.value < k:
      if not before_list:
        before_list = ListNode(current.value)
        before_head = before_list
      else:
        before_list.next = ListNode(current.value)
        before_list = before_list.next
    else:
      if not after_list:
        after_list = ListNode(current.value)
        after_head = after_list
      else:
        after_list.next = ListNode(current.value)
        after_list = after_list.next
    current = current.next

  if before_list and before_head:
    if after_list and after_head:
      before_list.next = after_head
    return before_head.to_list()
  else:
    if after_list and after_head:
      return after_head.to_list()
    else:
      return None


def partition_using_one_list(linked_list, k):
  current = linked_list
  if not current:
    return current
  new_list = ListNode(current.value)
  new_list_start = new_list
  current = current.next
  while current:
    # if value is less than k, then put it to the head. else,
    # put it in the end.
    if current.value < k:
      temp_list = new_list_start
      new_list_start = ListNode(current.value)
      new_list_start.next = temp_list
    else:
      new_list.next = ListNode(current.value)
      new_list = new_list.next
    current = current.next
  return new_list_start.to_list()


linked_list_a: ListNode = create_linked_list_from_list(
    [1, 2, 5, 3, 6, 7, 2, 5])
linked_list_b: ListNode = create_linked_list_from_list(
    [1, 2, 3, 2, 5, 6, 7, 5])

test_cases = [
    ((linked_list_a, 5), linked_list_b.to_list()),
]

run_tests(partition, test_cases)

linked_list_c: ListNode = create_linked_list_from_list(
    [1, 2, 5, 3, 6, 7, 2, 5])
linked_list_d: ListNode = create_linked_list_from_list(
    [2, 3, 2, 1, 5, 6, 7, 5])

test_cases = [
    ((linked_list_c, 5), linked_list_d.to_list()),
]

run_tests(partition_using_one_list, test_cases)
