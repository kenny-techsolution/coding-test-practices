import copy


def run_tests(solution_func, test_cases):
  func_name = solution_func.__name__
  print(f"Test result for {func_name}:")
  for (inputs, expected) in test_cases:
    input_string_list = []
    displayed_input = ""
    for input in inputs:
      input_string_list.append(str(input))
    displayed_input = ",".join(input_string_list)
    new_input = copy.deepcopy(inputs)
    result = solution_func(
        *new_input)  # Unpack the inputs tuple into the function arguments
    assert result == expected, f"Inputs:[{displayed_input}]  failed. Expected {expected}, got {result}."
    print(f"Inputs:[{displayed_input}] passed.")
