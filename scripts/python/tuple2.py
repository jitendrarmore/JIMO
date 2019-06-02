#!/usr/local/bin/python3

a = [10, 30, 20, 40, 50, 60, 70]
b = [10, 30, 40, 60, 80]

t = (10, 20, 30, 40, 50)
ts = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'xyz')

# the use of tuple() function

# when parameter is not passed

tuple1 = tuple()
print(tuple1)

# when an iterable(e.g., list) is passed

tuple2 = tuple(ts)
print(tuple2)


# when an iterable(e.g., dictionary) is passed

dict = { 1 : 'one', 2 : 'two' }
tuple2 = tuple(dict)
print(tuple2)

# when an iterable(e.g., string) is passed
string = 'thisisjitendramore'
tuple4 = tuple(string)
print(tuple4)
