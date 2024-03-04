def print_binary(num):
  binary_str = "."
  if num>=1 or num<=0:
    return "Error"
  while num>0:
    if len(binary_str)>=32:
      return "Error"
    
    num *=2
    if num>=1:
      binary_str +="1"
      num-=1
    else:
      binary_str+="0"
    print(binary_str)
  return binary_str

print(print_binary(0.72))
print(print_binary(0.625))