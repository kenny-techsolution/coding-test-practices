from stack import Stack
# stack with min method
#solution 1 - use a node class to capture min at each state.


class StackMin1(Stack):

  class MinNode:

    def __init__(self, value, min):
      self.value = value
      self.min = min

  def __init__(self):
    super().__init__()

  def push(self, value):
    #when push value, check if the min should be updated.
    min = self.min()
    node = self.MinNode(value, value if value < min else min)
    super().push(node)

  def min(self):
    if self.is_empty():
      return float('inf')
    node: StackMin1.MinNode = self.peek()
    return node.min


#stage 2 - use additional stack to record the min, more space efficient.
class StackMin2(Stack):

  def __init__(self):
    super().__init__()
    self.min_stack = Stack()

  def push(self, value):
    if self.min_stack.is_empty or value <= self.min_stack.peek():
      self.min_stack.push(value)
    super().push(value)

  def min(self):
    if self.min_stack.is_empty():
      raise Exception("stack has no minimum")
    return self.min_stack.peek()
