# three stack class.
# [ 0, 1, 2, 3, 4 ,5, 6, 7, 8]
# [ 0, 0, 0, 1, 1, 1, 2, 2, 2]

class FixedStacks:
  def __init__(self, stack_capacity):
    self.stack_capacity = stack_capacity
    self.values = [None]*(self.stack_capacity*3)
    self.sizes = [0]*self.stack_capacity
    
  def push(self, stack_num, value):
    # check if the stack is full
    # update the sizes
    if self.is_full(stack_num):
      raise Exception(f"stack {stack_num} is full")
    index = self.index_of_top(stack_num)
    self.sizes[stack_num] += 1
    self.values[index]=value

  def pop(self, stack_num)->int:
    # check if the stack is empty
    # update the sizes
    if self.is_empty(stack_num):
      raise Exception(f"stack {stack_num} is empty")
    index = self.index_of_top(stack_num)
    self.sizes[stack_num] -= 1
    value = self.values[index]
    self.values[index]=None
    return value 

  def peek(self, stack_num)->int:
    if self.is_empty(stack_num):
      raise Exception(f"stack {stack_num} is empty")
    index = self.index_of_top(stack_num)
    return self.values[index]

  def is_empty(self, stack_num)->bool:
    return self.sizes[stack_num] == 0

  def is_full(self, stack_num)->bool:
    return self.sizes[stack_num]==self.stack_capacity

  def index_of_top(self, stack_num):
    offset = stack_num * self.stack_capacity + self.sizes[stack_num]-1
    return offset

# psuedo code for FlexibleStacks
  