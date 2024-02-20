from stack import Stack

class SetOfStacks:
  def __init__(self):
    self.stacks = []
    self.stack_capacity = 5
  def push(self, value):
    # check if the last stack is full. or if last stack is none. 
    # if so, add new stack. 
    stack = self.last_stack()
    if not stack or stack.is_full():
      stack = self.add_new_stack()
    stack.push(value)
    
  def pop(self):
    # check if there is stack to pop, otherwise raise error 
    # after pop, if the last stack is empty, remove last stack
    stack = self.last_stack()
    if stack:
      value = stack.pop()
      if stack.is_empty():
        self.stacks.pop()
    else:
      raise Exception("there is no element to pop")
    return value

  def last_stack(self):
    if len(self.stacks) == 0:
      return None
    else:
      return self.stacks[len(self.stacks)-1]

  def add_new_stack(self):
    stack = Stack(self.stack_capacity)
    self.stacks.append(stack)
    return stack
    