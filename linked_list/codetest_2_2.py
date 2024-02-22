from testing.test_util import run_tests

from linked_list_class import create_linked_list_from_list


# Solution 1 using runner technique
def nth_to_last(linked_list, k):
  p1 = linked_list
  p2 = linked_list
  for i in range(k):
    if not p1:
      return None
    p1 = p1.next

  while p1.next:
    p1 = p1.next
    p2 = p2.next

  return p2.to_list()


linked_list_a = create_linked_list_from_list([1, 2, 5, 3, 6, 7, 2, 5])

test_cases = [
    ((linked_list_a, 3), [6, 7, 2, 5]),
]

run_tests(nth_to_last, test_cases)
