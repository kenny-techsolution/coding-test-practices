from typing import Optional


class ListNode:

  def __init__(self, value: int, next: Optional['ListNode'] = None):
    self.value: int = value
    self.next: Optional['ListNode'] = next

  def __str__(self):
    output_list = self.to_list()
    return str(output_list)

  def __json__(self):
    return self.to_list()

  # def __len__(self):
  #   return len(self.to_list())

  def to_list(self) -> list:
    output_list = []
    current = self
    while current:
      output_list.append(current.value)
      current = current.next
    return output_list


class PartialSum:

  def __init__(self, list_sum: Optional[ListNode] = None, carry: int = 0):
    self.list_sum: Optional[ListNode] = list_sum
    self.carry: int = carry


def pad_list(list: ListNode, padding: int):
  for _ in range(padding):
    list = insert_before(list, 0)
  return list


def insert_before(list, data: int):
  node = ListNode(data)
  node.next = list
  return node


def create_linked_list_from_list(input_list) -> ListNode:
  head = None
  current = None
  for i in input_list:
    if head is None:
      head = ListNode(i)
      current = head
    else:
      current.next = ListNode(i)
      current = current.next
  return head


def get_linked_list_as_list(linked_list):
  output_list = []
  current = linked_list
  while current:
    output_list.append(current.val)
    current = current.next
  return output_list
