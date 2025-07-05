# write a function to remove duplicates from a list 

def remove_duplicate(lst):
  # convert list to a set, a set do not allow duplicates
  duplicate_list = set(lst)

  # convert it back to a list
  return list(duplicate_list)

lst = [1,1,2,2,3,3,4,4]
new_lst = remove_duplicate(lst)
print(new_lst)
