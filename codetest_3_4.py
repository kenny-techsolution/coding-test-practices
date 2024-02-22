from stack import Stack

class MyQueue:
  def __init__(self):
    self.newest_stack = Stack()
    self.oldest_stack = Stack()

  def add(self, value):
    self.newest_stack.push(value)
  def remove(self):
    if self.oldest_stack.size==0:
      while self.oldest_stack.size >0:
        value = self.newest_stack.pop()
        self.oldest_stack.push(value)
    else:
      self.oldest_stack.pop()
    
