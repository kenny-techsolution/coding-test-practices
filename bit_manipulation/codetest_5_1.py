def insert_m_to_n(n, m, i, j):
  # assuming j > i
  # step 1. create mask for i and j 
  # create mask with 1s followed by 0 starting i
  # create mask with 0s followed by 1 starting j-1
  left_mask = (~0)<< (j +1)
  right_mask = (1<<i)-1  
  # step 2. clear N from i to j
  mask = left_mask | right_mask
  n &= mask
  
  # step 3. merge M to N. 
  # 3.1 shift the M by 
  m <<= i
  # 3.2 merge M & N
  return m | n

n = int("10000000000",2)
m = int("10011", 2)

result = insert_m_to_n(n, m, 2, 6)

expected = int("10001001100", 2)
print(bin(result), "same as expected?:", result==expected)