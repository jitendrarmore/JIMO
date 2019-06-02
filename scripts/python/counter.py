from collections import Counter

def dup_char(input):
  wc = Counter(input)
  j = -1

  for i in wc.values():
    j = j + 1
    if (i > 1):
      print wc.keys() [j],

if __name__ == '__main__':
  input = 'jitendraramdasmore'
  dup_char(input)
