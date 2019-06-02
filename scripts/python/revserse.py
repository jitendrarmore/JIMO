# reverse word of string

s = ' i like mango and  orange'
# orange and mango like I

print s.split() # splits on whitespace tab , newline , multiple spaces

r = s.split()[::-1] # [] Index operator : start : stop : steps how many step you want to index
print ' '.join(r) # [::-1] cannonical form



print ' '.join(s.split()[::-1])
