from test_util import run_tests

from linked_list_class import create_linked_list_from_list


#solution 1
def delete_dups(linked_list) -> list:
  # iterate through linked list
  # add the element into set.
  # if already in the set, remove the dup
  node_set = set()
  prev = linked_list
  current = linked_list
  while current:
    if current.val not in node_set:
      node_set.add(current.val)
      prev = current
    else:
      prev.next = current.next
    current = current.next
  return linked_list.to_list()


#solution 2
def delete_dups_runner(linked_list) -> list:
  current = linked_list
  while current:
    runner = current
    prev = runner
    while runner:
      if current.val == runner.val:
        prev.next = runner.next
      else:
        prev = runner
      runner = runner.next
    current = current.next
  return linked_list.to_list()


linked_list_a = create_linked_list_from_list([1, 2, 5, 3, 6, 7, 2, 5])

test_cases = [
    ((linked_list_a, ), [1, 2, 5, 3, 6, 7]),
]

run_tests(delete_dups, test_cases)
run_tests(delete_dups_runner, test_cases)
