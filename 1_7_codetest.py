from test_util import run_tests


def rotate_matrix(matrix):
  #step1 check it's non zero or symatric matrix
  matrix_len = len(matrix)
  if matrix_len > 0 and matrix_len != len(matrix[0]):
    return False
  for layer in range(0, matrix_len // 2, 1):
    # first item's index of the current layer
    first = layer
    # last item's index of the current layer
    last = matrix_len - 1 - first
    for i in range(first, last, 1):
      #relative position of the current layer
      offset = i - first
      # move top to temp
      top_temp = matrix[first][i]
      # move left -> top
      matrix[first][i] = matrix[last - offset][first]
      # move bottom -> left
      matrix[last - offset][first] = matrix[last][last - offset]
      # move right -> bottom
      matrix[last][last - offset] = matrix[i][last]
      # move temp -> right
      matrix[i][last] = top_temp
  return matrix


test_cases = [
    (([[1, 2], [3, 4]], ), [[3, 1], [4, 2]]),
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
]

run_tests(rotate_matrix, test_cases)
