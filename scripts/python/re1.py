```# regular expressions in python I
# reqular expression with search fuctions

import re
s = 'Today is wednesday and tommorrow is thursday'
# re.match (pattern, string, flag<optiona>)
p = re.match('Today.*', s)
if p:
    print 'found match'
else:
    print 'no match'

# regular expression substitution

x = 'this is 1234 4566' #
#re.sub() #Pattern replacement , string
# for digit use '\d' and non-digit use '\D'
a = re.sub('\d.*', '', x )
print a
b = re.sub('\D*', '', x )
print b

# \w+s it means that word is getting end with 's' which you can match and replace using re.sub fuction

#############################################
# re.search pattern is as given above
# \w = word character
# + one or more = this is for caracter
# . = any one characher
# \. = the dot character
#\ is used to escape a character

email = 'jmore@expedia.com'
email1 = 'jeetu.more@gmail.in'
id = re.search('\w+@\w+\.com', email)
id = re.search('\w+\.\w*@\w+\.\w+', email1)
if id:
    print ' email if found', id.group()

elif id1:
    print ' email if found', id1.group()
else:
    print ' email is not found'```
