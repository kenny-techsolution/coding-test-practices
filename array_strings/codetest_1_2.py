def is_permutation_sorted(str1, str2):
  if len(str1) != len(str2):
    return False
  sorted_char1 = sorted(str1)
  sorted_char2 = sorted(str2)
  return sorted_char1 == sorted_char2


def is_permutation_identical_char_count(str1, str2):
  if len(str1) != len(str2):
    return False
  char_count_list = [0] * 128
  for char in str1:
    ascii_val = ord(char)
    char_count_list[ascii_val] += 1
  for char in str2:
    ascii_val = ord(char)
    char_count_list[ascii_val] -= 1
    if char_count_list[ascii_val] < 0:
      return False
  return True


def is_permutation_hashmap(str1, str2):
  if len(str1) != len(str2):
    return False
  char_count = {}
  for char in str1:
    char_count[char] = char_count.get(char, 0) + 1
  for char in str2:
    char_count[char] = char_count.get(char, 0) - 1
    if char_count[char] < 0:
      return False
  return True


value1 = is_permutation_sorted("abc", "cbv")
value2 = is_permutation_sorted("abc", "cba")
value3 = is_permutation_hashmap("abc", "cbv")
print(value1)
print(value2)
print(value3)
