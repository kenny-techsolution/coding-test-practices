from testing.test_util import run_tests
from typing import Optional
from linked_list_class import ListNode, PartialSum, create_linked_list_from_list, insert_before, pad_list


def intersection(l1: ListNode, l2: ListNode) -> bool:
  # find the length of two list
  head1 = l1
  head2 = l2
  p1 = l1
  p2 = l2
  len1 = 0
  len2 = 0
  while p1:
    len1 += 1
    p1 = p1.next
  while p2:
    len2 += 1
    p2 = p2.next
  p1 = head1
  p2 = head2
  # find the difference in two list, then forward the pointer of the longer list so that pointer start at the same nth node from the last node as the shorter list.
  diff_len = len1 - len2
  if diff_len > 0:
    while diff_len > 0:
      p1 = p1.next
      diff_len -= 1
    pass
  else:
    while diff_len < 0:
      p2 = p2.next
      diff_len += 1
    pass

  # move both pointers to see if they collide.
  while p1 and p2:
    if p1 == p2:
      return True
    p1 = p1.next
    p2 = p2.next

  return False


linked_list_a: ListNode = create_linked_list_from_list(
    [1, 2, 5, 3, 6, 7, 2, 5])
linked_list_b: ListNode = create_linked_list_from_list([7, 5])

current = linked_list_b
while current.next:
  current = current.next
current.next = linked_list_a

test_cases = [
    ((linked_list_a, linked_list_b), True),
]

run_tests(intersection, test_cases)
