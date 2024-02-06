from test_util import run_tests


def isRotation(str1, str2):
  return str2 in (str1 + str1)


test_cases = [(("erbottlewat", "waterbottle"), True),
              (("erbottlewat", "watebottle"), False)]
run_tests(isRotation, test_cases)
