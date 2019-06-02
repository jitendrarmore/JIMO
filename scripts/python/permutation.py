from itertools import permutations

def allpermutations(str):
  permList = permutations(str)

  for perm in list(permList):
    print(''.join(perm))

if __name__=="__main__":
  str = 'pankaj'
print(allpermutations(str))
