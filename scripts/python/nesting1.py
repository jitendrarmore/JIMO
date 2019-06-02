# for loop nesting 
# How to use datetime 
# 10^6 is microseconds means = 1 second
# read docs.python.org
import datetime
# hr minutes and seconds 
time = datetime.time(10, 10, 30)
print time 
print 'hour', time.hour
print 'minutes', time.minute
print 'seconds', time.second

# year month and day
date = datetime.date(2016, 12, 10)
print date
print 'year', date.year
print 'month', date.month
print 'day', date.day


datetimenow = datetime.datetime.now()
print datetimenow

#datenow = datetime.date.now()
#print datenow

resolution =  datetime.datetime.resolution()
print resolution
