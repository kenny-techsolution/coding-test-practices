from testing.test_util import run_tests


def count_ways(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


def count_ways_memo(n):

  def count_ways_memo_helper(n, memo):
    if n < 0:
      return 0
    if n == 0:
      return 1
    if memo[n] == -1:
      memo[n] = (count_ways_memo_helper(n - 1, memo) +
                 count_ways_memo_helper(n - 2, memo) +
                 count_ways_memo_helper(n - 3, memo))
    return memo[n]

  return count_ways_memo_helper(n, [-1] * (n + 1))


# if n = 4
#     cw(3)+cw(2)+c(1)
# cw(3)
# cw(2)+c(1)+c(0) => c(2)+c(1)+1 =>
# cw(2) => c(1)+c(0)+c(-1) => c(1)+1+0
# cw(1)=> c(0)+c(-1)+c(-2)=> 1+0+0

test_cases = [
    ((5, ), 13),
]

run_tests(count_ways, test_cases)
run_tests(count_ways_memo, test_cases)
