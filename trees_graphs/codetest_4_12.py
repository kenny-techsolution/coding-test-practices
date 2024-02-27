def count_path_with_sum(root, target):
  path_count_map = {}

  return count_path_with_sum_helper(root, target, 0, path_count_map)
    
def count_path_with_sum_helper(root, target, running_sum, path_count_map):
  if not root:
    return 0

  # count paths with sum ending at the current node
  running_sum+= root.value
  sum = running_sum - target
  total_paths = path_count_map.get(sum, 0)
  
  # if running_sum equals target sum, then one additional path starts at root. 
  if running_sum == target:
    total_paths+=1
  
  # increment path_count recurse, then decrement path count.
  increment_hashtable(path_count_map, running_sum, 1)
  total_paths+= count_path_with_sum_helper(
    root.left, target, running_sum, path_count_map)
  total_paths+= count_path_with_sum_helper(
    root.left, target, running_sum, path_count_map)
  increment_hashtable(path_count_map, running_sum, -1)

def increment_hashtable(path_count_map, key, delta):
  new_count = path_count_map.get(key, 0) + delta
  if new_count == 0:
    del path_count_map[key]
  else:
    path_count_map[key]= new_count
  
  
  