from stack import Stack

def sort(stack:Stack):
  # create another stack as the sorted stack
  sorted_stack = Stack()
  # peek top of sorted_stack, compare it with temp, if tmp is larger, then put tmp onto sorted_stack.
  while stack.is_empty:
    tmp = stack.pop()
    while sorted_stack.is_empty and tmp > sorted_stack.peek():
      stack.push(sorted_stack.pop())
    sorted_stack.push(tmp)  

  while sorted_stack.is_empty():
    stack.push(sorted_stack.pop())