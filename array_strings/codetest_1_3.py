# solve with char list
def replace_space_c_method(str):
  #step 1. first loop to check how many space there are
  char_list = list(str)
  space_count = 0
  index = 0
  for char in char_list:
    if char == " ":
      space_count += 1

  new_len = len(str) + space_count * 2
  print(new_len, len(str))
  #step 2. create char list using the new len
  new_char_list = [" "] * new_len

  #step 3. copy value backward to the new char list
  for i in range(len(char_list) - 1, -1, -1):
    char = char_list[i]
    if char == " ":
      new_char_list[index - 1] = '0'
      new_char_list[index - 2] = '2'
      new_char_list[index - 3] = '%'
      index -= 3
    else:
      new_char_list[index - 1] = char
      index -= 1
  return "".join(new_char_list)


def replace_space_python_method(str):
  return str.replace(" ", "%20")


value1 = replace_space_c_method("this is a great plan")
value2 = replace_space_python_method("this is a great plan")
print(value2)
