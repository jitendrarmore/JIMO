# for loop nesting 
# how to use index operator 
# Break statement is also being used.
b = ['b', 'c', 'd', 'e', 'f', 'g', 'h']
a = [1, 2, 3, 4, 5, 6, 7]
for i in range(0, len(a)):
    if i == 5:
        break # mean value is equal to 4
    print i, a[i]

d = [1, 2, 3, 4, 5, 6, 7]
value = 0
while value < len(b):
    if value == 3:
        break # mean value is equal to 4
    print b[value]
    value = value + 1
     

# for loop nesting 
# Used of conntinue statement in loop # mostly this is being used in loop
b = ['b', 'c', 'd', 'e', 'f', 'g', 'h']
a = [1, 2, 3, 4, 5, 6, 7]
def number(test):
    for i in test:
        if i < 5:
            continue# mean when condition is true will go back to if statement else next
        return i 
print (number(a))
