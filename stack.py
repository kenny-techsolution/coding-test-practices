class Stack:

  def __init__(self):
    self.values = []
    self.size = 0

  def push(self, value):
    self.values.append(value)

  def pop(self):
    if len(self.values) == 0:
      raise Exception("stack is empty")
    value = self.values.pop()
    return value

  def peek(self):
    if self.is_empty():
      raise Exception("stack is empty")
    return self.values[len(self.values) - 1]

  def is_empty(self) -> bool:
    return len(self.values) == 0
