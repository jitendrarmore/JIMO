#!/usr/bin/python
'''
#import datetime

print date.today()
'''
from datetime import date
from datetime import datetime

# time delta this means differrent between two dates
aa = date(1986,9,6)
bb = date(2018,9,28)

print (bb-aa).days

a = datetime(1986,9,6,9,20,21)
b = datetime(2018,9,28,12,20,44)

print (b-a)
print (b-a).days
print (b-a).seconds
