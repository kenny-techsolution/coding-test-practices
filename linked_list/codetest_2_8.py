from testing.test_util import run_tests
from typing import Optional
from linked_list_class import ListNode, PartialSum, create_linked_list_from_list, insert_before, pad_list


def detect_loop(head: ListNode) -> bool:
  fast, slow = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if fast.value == slow.value:
      return True
  return False


linked_list_a: ListNode = create_linked_list_from_list([1, 2, 5, 3, 6, 7])

current = linked_list_a
while current.next:
  current = current.next
current.next = linked_list_a.next

test_cases = [
    ((linked_list_a, ), True),
]

run_tests(detect_loop, test_cases)
