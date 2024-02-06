def is_unique_fixed_array(str):
  if len(str) > 128:
    return False

  char_set = [False] * 128
  for i in str:
    index = ord(i)
    if char_set[index]:
      return False
    else:
      char_set[index] = True
  return True


def is_unique_bit_vector(str):
  if len(str) > 128:
    return False

  checker = 0
  for i in str:
    index = ord(i) - ord("a")
    if (checker & (1 << index)) == 1:
      return False
    else:
      checker |= (1 << index)
  return True


def is_unique_sorted(str):
  if len(str) > 128:
    return False
  sorted_char = sorted(str)
  for i in range(len(sorted_char) - 1):
    if sorted_char[i] == sorted_char[i + 1]:
      return False
  return True


value = is_unique_fixed_array("soijlkgS")
value2 = is_unique_bit_vector("absdflkjia")
value3 = is_unique_sorted("abcda")
print(value3)
