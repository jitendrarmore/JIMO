#String formating 
# Old : '%s %s' % ('one' , 'two')
# New : '{} {}'.format('one', 'two')
# the below print is look like print place strings like index
#website for refer more string example http://pyformat.info
'''
print('{1} {0}'.format('one', 'two'))
print('{:a>10}'.format('test'))
print('{:>10}'.format('test'))
print('{:a<10}'.format('test'))
print('{:<10}'.format('test'))
