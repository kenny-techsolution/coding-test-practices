from testing.test_util import run_tests


def is_palindrome_hashtable(str):
  #step 1. build a hash table
  char_frequency_table = {}
  # convert to lowercase since it's case insensitive.
  lowercase_str = str.lower()
  for char in lowercase_str:
    if char.isalpha():
      char_frequency_table[char] = char_frequency_table.get(char, 0) + 1
  #step 2. loop the hashtable to see if the odd number of character is no more than 1.
  oddFound = False
  for key in char_frequency_table:
    count = char_frequency_table[key]
    if count % 2 == 1:
      if oddFound:
        return False
      oddFound = True
  return True


def is_palindrome_hashtable_tweak(str):
  #check a hash table while it's being built.
  char_frequency_table = {}
  lowercase_str = str.lower()
  odd_count = 0
  for char in lowercase_str:
    if char.isalpha():
      char_frequency_table[char] = char_frequency_table.get(char, 0) + 1
      if char_frequency_table[char] % 2 == 1:
        odd_count += 1
      else:
        odd_count -= 1
  return odd_count <= 1


def toggleNthBit(number, n):
  mask = 1 << n
  return number ^ mask


def hasExactlyOneBitSet(number):
  invert = number - 1
  return (number & invert) == 0


def is_palindrome_bit_vector(str):
  # step 1. construct the bit vector
  bit_vector = 0
  lowercase_str = str.lower()
  ord_a = ord("a")
  for char in lowercase_str:
    if char.isalpha():
      index = ord(char) - ord_a
      bit_vector = toggleNthBit(bit_vector, index)
  # step 2. check if the bit vector is 0 , or just 1 one.
  return bit_vector == 0 or hasExactlyOneBitSet(bit_vector)


# value1 = is_palindrome_hashtable("Tact Coa")
# print(value1)
# value2 = is_palindrome_hashtable_tweak("Tact KCoa")
# print(value2)
# value3 = is_palindrome_bit_vector("Tact KCoa")
# print(value3)

test_cases = [
    (("tact Coa", ), True),
    (("Tact KCoa", ), False),
]

run_tests(is_palindrome_hashtable, test_cases)
run_tests(is_palindrome_hashtable_tweak, test_cases)
run_tests(is_palindrome_bit_vector, test_cases)
