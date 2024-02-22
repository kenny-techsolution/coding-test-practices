class Stack:

  def __init__(self, limit=None):
    self.limit = limit 
    self.values = []
    self.size = 0

  def push(self, value):
    if self.is_full():
      self.values.append(value)

  def pop(self):
    if self.is_empty():
      raise Exception("stack is empty")
    value = self.values.pop()
    return value

  def peek(self):
    if self.is_empty():
      raise Exception("stack is empty")
    return self.values[len(self.values) - 1]

  def is_empty(self) -> bool:
    return len(self.values) == 0

  def is_full(self) -> bool:
    if not self.limit:
      return False
    else:
      return len(self.values) >= self.limit
