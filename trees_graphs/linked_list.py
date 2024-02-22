class ListNode:

  def __init__(self, value=None, next_node=None):
    self.value = value  # value can be any object
    self.next = next_node


class LinkedList:

  def __init__(self):
    self.head = None

  def append(self, value):
    """Append a new node with the given value (any object) to the end of the list."""
    if not self.head:
      self.head = ListNode(value)
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = ListNode(value)

  def print_list(self):
    """Print the contents of the linked list."""
    current = self.head
    while current:
      print(repr(current.value), end=" -> ")
      current = current.next
    print("None")  # End of the list
