#list fuction 
#list is a data structure
#Do your code as follow 

a = [ 'abc', 'def', 'ghi', 'jkl', 'mno']
b = [1, 2, 3, 4, 5]


i = 0
while i < 5: #infinite loop
    print a[i], b[i]  # indexing the ith element 
    i = i + 1 # increasing a loop value by +1
    
print a
print 'fist index of', a[0]
print 'lengh of list', len(a)
print 'last element of', a[3], a[-2]
print 'last element of', a[2], a[N-2]

#==============
#in order to append at the end of string you can use append
'''
c = [ 'abc', 'def', 'ghi', 'jkl', 'mno']
c.append('qrs')
c.append('tvu')
c.remove('abc')
c[2] = 'xyz'
del c[4]
print c`
