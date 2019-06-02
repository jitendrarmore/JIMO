#!/usr/local/bin/python3

a = 'jitendra Ramdas More'


def reverse(a):
  str = ""
  for i in a:
    str = i + str
  return str

print(reverse(a))

s = 'jitendra Ramdas More'

def reverser(s):
  if len(s) == 0:
    return s
  else:
    return reverser(s[1:]) + s[0]


print(reverser(a))
string = ['b', 'c', 'd', 'e', 'f', 'g', 'h']

def reves(string):
  string = string[::-1]
  return string


print(reves(string))
