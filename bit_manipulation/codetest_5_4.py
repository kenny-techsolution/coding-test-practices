def next_bigger(n):
  # find c0, and c1
  # determine p. 
  c = n
  c0=0
  c1=0
  print("test1")
  while (c&1)==0 and c!=0:
    print("get 0")
    c0+=1
    c>>=1
  
  while (c&1)==1:
    print("get 1")
    c1+=1
    c>>=1
  print("test")
  if (c0+c1) == 31 or (c0+c1)==0:
    return -1
  p = c0+c1
  # filp p from 0 to 1.
  a = 1 << p
  n = n|a
  
  # flip all digits to zero on the right of p. 
  a = 1 << p
  b = a-1
  mask = ~b
  n = n & mask
  # put C1-1 one to right
  a = 1 << (c1-1)
  b = a-1
  n = n | b
  return n

def next_smaller(n):
  # calculate c0 and c1. 
  c=n
  c0=0
  c1=0
  while (c&1)==1 and c!=0:
    c1+=1
    c>>=1
  while (c&1)==0:
    c0+=1
    c>>=1

  # handle special condition
  if (c0+c1)==31 and (c0+c1)==0:
    return -1

  #set all bits on the right of p, and including p to zeros 
  p = c0+c1

  a = 1 <<(p+1)
  b = a-1
  mask = ~b
  n = n&mask

  #set c1+1 of one immediately right of p. 
  # create c1+1 of ones. 
  a = 1<<(c1+1)
  b = a-1
  b = b<<(c0-1)
  n = n|b
  
  return n

n = int("11011001111100",2)
result = next_bigger(n)
expected = int("11011010001111",2)
print(bin(result), "is same as expected?", expected, result == expected)

n = int("10011110000011",2)
result = next_smaller(n)
expected_binary = "10011101110000"
expected = int("10011101110000",2)
print(bin(result),expected_binary, "is same as expected?", expected, result == expected)