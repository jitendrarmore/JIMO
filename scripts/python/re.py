# regular expressions in python I
# reqular expression with search fuctions

import re
s = 'Today is wednesday and tommorrow is thursday'
# re.search (pattern, string, flag<optiona>)
p = re.search('(.*) and (.*)', s)
if p:
    print 'Found:', p.group()
    print 'Group1:', p.group(1), ':' , p.group(1).capitalize()
    print 'Group2:', p.group(2), ':' , p.group(2).capitalize()
else:
    print "not fund"

#############################################################################
# regular expression part 2
# in order to match any string pattern then use regular expression
# pyformat.info

#import re
string  = 'Today is wedenday And tommarrow is Thursday'
z = re.search('.* and .*', string, re.I)
# # re.search (pattern, string, flag<optiona>)
# . Match any character
# * Zero or more
if z:
    print ' pattern found'
else:
    print ' no match'


#############################################################################

s1 = 'my name is khan and i am an Indian'
s2 = 'and'
y = re.search('.*and.*', s2 )
# # re.search (pattern, string, flag<optiona>)
if y:
    print ' pattern found'
else:
    print ' no match'

#############################################################################

s3 = 'Today my name is khan and i am an Indian'
s4 = 'and'
x = re.match('Today(.*)(.*)and(.*)' , s3)
if x:
    print ' pattern found' , x.group()
    print ' found match' , x.group(1)
    print ' found match' , x.group(2)
else:
    print ' no match'
