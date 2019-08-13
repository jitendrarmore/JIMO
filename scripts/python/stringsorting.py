def sortingstring(string):
  sortstring = sorted(string)
  sortedstring = ""
  for i in sortstring:
    sortedstring += i
  print(sortedstring)

#sortingstring('rajes34singh')

a = sorted(['h4ow',' h8i', 'a23re','rajes34singh', 'yo76u'])

for inputlist in a:
  print(sortingstring(inputlist))
