def longest_sequence(n):
  sequences = get_alternative_sequences(n)
  length = find_longest_sequence(sequences)
  return length

# step 1. construct of list of consecutive 0 and 1 counts from 0 to nth position. 
def get_alternative_sequences(n):
  search_for = 0
  sequences = []
  count = 0

  for i in range(32):
    if (n&1) == search_for:
      count+=1
    else:
      sequences.append(count)
      count = 1
      search_for = n&1
    n>>=1
  return sequences
# step 3. find the maximum length 
def find_longest_sequence(sequences):
  i = 1
  max_length = 0
  while i < (len(sequences)-2):
    zero_count = sequences[i+1]
    if zero_count == 1:
      length = sequences[i]+sequences[i+2]+1
      max_length = max(max_length, length)
      i+=2
  return max_length

a = int("11011101111",2)
print(longest_sequence(a))


