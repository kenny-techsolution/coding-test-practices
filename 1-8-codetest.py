from test_util import run_tests


def zero_matrix(matrix):
  # step 1 create row and column array to flag zero row and columns
  rows = [False] * len(matrix)
  columns = [False] * len(matrix[0])
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        rows[i] = True
        columns[j] = True
  # step2 set entire row to 0.
  for i in range(len(rows)):
    if rows[i]:
      for j in range(len(matrix[0])):
        matrix[i][j] = 0
  for j in range(len(columns)):
    if columns[j]:
      for i in range(len(matrix)):
        matrix[i][j] = 0
  return matrix


# without using the additional rows and columns array
def zero_matrix_improved(matrix):
  #step 1. check if first row has any zero
  first_row_has_zero = False
  for j in range(len(matrix[0])):
    if matrix[0][j] == 0:
      first_row_has_zero = True
      break
  #step 2. check if first columns has any zero
  first_columns_has_zero = False
  for i in range(len(matrix)):
    if matrix[i][0] == 0:
      first_columns_has_zero = True
      break

  #step 3. iterate through the rest of matrix to identify zero
  #flag it to the first row and column
  for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
      if matrix[i][j] == 0:
        print(i, j)
        matrix[i][0] = 0
        matrix[0][j] = 0
  #step 4. set column to zero based on the first row flagging.
  for j in range(len(matrix[0])):
    if matrix[0][j] == 0:
      set_column_zero(matrix, j)

  #step 5. set row to zero based on the first column flagging
  for i in range(len(matrix)):
    if matrix[i][0] == 0:
      set_row_zero(matrix, i)
  #step 6. set row to zero if the first row has zero.
  if first_row_has_zero:
    set_row_zero(matrix, 0)

  #step 7. set row to zero if the first row has zero.
  if first_columns_has_zero:
    set_column_zero(matrix, 0)

  return matrix


def set_row_zero(matrix, row_index):
  for j in range(len(matrix[0])):
    matrix[row_index][j] = 0
  return matrix


def set_column_zero(matrix, column_index):
  for i in range(len(matrix)):
    matrix[i][column_index] = 0
  return matrix


test_cases = [
    (([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 0],
        [1, 1, 1, 1, 1],
    ], ), [
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
    ]),
]

run_tests(zero_matrix, test_cases)
run_tests(zero_matrix_improved, test_cases)
