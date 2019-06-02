list3 = 'listen'
list4 = 'silent'

def find_string_anagram(list3, list4):
  if(sorted(list3) == sorted(list4)):
    return 'string is anagram'
  else:
    return 'string is not anagrams'

print(find_string_anagram(list3, list4))
