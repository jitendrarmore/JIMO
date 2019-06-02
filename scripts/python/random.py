import random

list = [2, 3, 5, 6, 10]

def randomize(list):
  random.shuffle(list)
  print("shuffeling :" , list)

randomize(list)
