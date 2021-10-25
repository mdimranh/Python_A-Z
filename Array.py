from array import *

vals = array("i", [5, 9, -8, 4, 2])
print(vals)
print(vals.buffer_info())    #address, size

print(vals.typecode)    #type

for i in vals:
    print(i)

name = array('u', ['a', 'e', 'i'])

for e in name:
    print(e)

vals.reverse()
print(vals)

newArray = array(vals.typecode, [a*a for a in vals])

