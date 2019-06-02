# tuple is imutable data type

a = (1, 2, 'apple', 'banana', 'mango')
print a

print a[1], a[3]
print len(a)

print a[0:3] # this is for range and doesn't include last two elements


# relation between list and tuple

# list is mutable and tuple is non-mutable
# both are sequance data structure
# you can look at any diamentional of data
# sequence Types - str, unicode, list, tuple,
# it is also support comparsion and this is compared lexicographically which mean tye and lenth should be same

x = (1, 2, 3, 4, 5, 4, 4)
y = [10, 11, 12, 13, 14, 15]
print max(x), max(y)
print min(x), min
print len(x)
print x.index(4)

print x.count(4)  # this will be count and tell you how many times this is in the list
# these are associated data structure
# tuple is a buit in fuction
# convert from tuple to list and vice versa tuple() is used and list [] is being used

print x
q = list(x)
print q

r = tuple(y)
print r
