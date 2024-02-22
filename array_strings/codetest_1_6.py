from testing.test_util import run_tests


def compress(input_str):
  compressed_str = ""
  repeat_count = 0
  for i in range(len(input_str)):
    repeat_count += 1
    if i + 1 >= len(input_str) or input_str[i] != input_str[i + 1]:
      compressed_str += (input_str[i] + str(repeat_count))
      repeat_count = 0
  return compressed_str


def compress_list_method(input_str):
  compressed_str_list = []
  repeat_count = 0
  for i in range(len(input_str)):
    repeat_count += 1
    if i + 1 >= len(input_str) or input_str[i] != input_str[i + 1]:
      compressed_str_list.append((input_str[i] + str(repeat_count)))
      repeat_count = 0
  return "".join(compressed_str_list)


test_cases = [
    (("ttaaabcccl", ), "t2a3b1c3l1"),
]
run_tests(compress, test_cases)
run_tests(compress_list_method, test_cases)
