from testing.test_util import run_tests

def bit_swapped_required(a, b):
  # XOR will give the bit that are different between two digit.
  c = a^b
  count = 0
  # count the digit that are 1.
  while c!=0:
    if c&1==1:
      count+=1  
    c>>=1
  return count


# this trick basically, remove the least significant 1 to 0. 

def bit_swapped_required_optimized(a, b):
  # XOR will give the bit that are different between two digit.
  c = a^b
  count = 0
  # count the digit that are 1.
  while c!=0:
    count+=1  
    c=c&(c-1)
  return count


test_cases = [
  ((29,15, ), 2),
]

run_tests(bit_swapped_required, test_cases)

run_tests(bit_swapped_required_optimized, test_cases)