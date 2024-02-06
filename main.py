import os

for filename in os.listdir('.'):
  if filename.endswith("-codetest.py"):
    print(filename)
    exec(open(filename).read())
