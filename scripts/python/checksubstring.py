def is_starts_or_ends_with(str,substr):
  if str[0] == substr:
    print(substr, ' is a Prefix')
  elif str[-1] == substr:
    print(substr, 'is a Suffix')
  else:
    print(substr, ' is neigher Prefix not Suffix')

a = ['h4ow','h8i', 'a23re','rajes34singh', 'yo76u']
substring = ['h', 'i', 'e', 'r', 'o']

for (inputlist,substring) in zip(a, substring):
  is_starts_or_ends_with(inputlist, substring)
