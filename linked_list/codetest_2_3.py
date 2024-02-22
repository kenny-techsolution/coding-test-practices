from testing.test_util import run_tests
from typing import Optional
from linked_list_class import ListNode, create_linked_list_from_list


def delete_node(linked_node):
  # need to handle if the node
  # the first node -
  # the last node - last node is node.next == None
  if not (linked_node and linked_node.next):
    print(linked_node.val)
    return False

  linked_node.value = linked_node.next.value
  linked_node.next = linked_node.next.next

  return linked_node.to_list()


linked_list_a: ListNode = create_linked_list_from_list(
    [1, 2, 5, 3, 6, 7, 2, 5])
linked_list_b: ListNode = create_linked_list_from_list([1, 2, 3, 6, 7, 2, 5])

linked_list_node_a: Optional[ListNode] = linked_list_a.next.next
linked_list_node_b: Optional[ListNode] = linked_list_b.next.next

test_cases = [
    ((linked_list_node_a, ), linked_list_node_b.to_list()),
]

run_tests(delete_node, test_cases)
