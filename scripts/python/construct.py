# for loop nesting 
# how to use index operator 
# 
b = ['b', 'c', 'd', 'e', 'f', 'g', 'h']
a = [1, 2, 3, 4, 5, 6, 7]
for i in range(0, len(a)):
    print i, a[i]

d = [1, 2, 3, 4, 5, 6, 7]
value = 0
while value < len(d):
    print d[value]
    value = value + 1
