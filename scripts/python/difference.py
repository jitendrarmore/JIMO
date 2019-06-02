def difference(list1, list2):
  return (list(set(list1) - set(list2)))

print(difference(list1, list2))



def diff(list1, list2):
  list_diff = [i for i in list1 + list2 if i not in list1 or i not in list2 ]
  return list_diff

print(diff(a, b))
