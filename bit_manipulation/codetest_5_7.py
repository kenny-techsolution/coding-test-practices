from testing.test_util import run_tests

def pairwise_swap(n):
  print(bin(n))
  # mask for odd bit 
  odd_mask = 0x55555555
  # mask for even bit 
  even_mask = 0xAAAAAAAA

  merged= ((n&odd_mask)<<1)|((n&even_mask)>>1)
  return merged

# bin(5) =  101
# bin(10)= 1010

test_cases = [
  ((5, ), 10),
]

run_tests(pairwise_swap, test_cases)