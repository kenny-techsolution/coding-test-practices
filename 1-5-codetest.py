from test_util import run_tests


def one_away(str1, str2):
  str1_len = len(str1)
  str2_len = len(str2)
  if str1_len == str2_len:
    return oneEditReplace(str1, str2)
  elif (str1_len - 1) == str2_len:
    return oneEditInsert(str1, str2)
  elif (str1_len + 1) == str2_len:
    return oneEditInsert(str2, str1)
  else:
    return False


def oneEditReplace(str1, str2):
  found_difference = False
  for i in range(len(str1)):
    if str1[i] != str2[i]:
      if found_difference:
        return False
      found_difference = True
  return True


# check if you can insert a character to str1 to make str2
def oneEditInsert(str1, str2):
  index1 = 0
  index2 = 0
  while index1 < len(str1) and index2 < len(str2):
    if str1[index1] != str2[index2]:
      if index1 != index2:
        return False
      index2 += 1
    else:
      index1 += 1
      index2 += 1
  return True


def one_away_combined_way(str1, str2):
  str1_len = len(str1)
  str2_len = len(str2)
  found_difference = False
  if abs(str1_len - str2_len) > 1:
    return False
  # shorthand for if else , for setting value.
  before_edit_string, after_edit_string = (
      str2, str1) if str1_len > str2_len else (str1, str2)
  index1 = 0
  index2 = 0
  while index1 < len(before_edit_string) and index2 < len(after_edit_string):
    if str1[index1] != str2[index2]:
      if found_difference:
        return False
      found_difference = True
      # On replace, move shorter pointer, this is the trick.
      if str1_len == str2_len:
        index1 += 1
    else:
      index1 += 1
    index2 += 1
  return True


test_cases = [
    (("abc", "abcd"), True),
    (("abc", "ab"), True),
    (("abc", "cbc"), True),
    (("abc", "cbccv"), False),
]

# Run the tests
run_tests(one_away, test_cases)
run_tests(one_away_combined_way, test_cases)
