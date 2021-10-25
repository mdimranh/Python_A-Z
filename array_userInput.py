
from array import *

arr = array('i', [])

a = int(input("Enter the length of array : "))

for i in range(a):
    x = int(input("Enter value : "))
    arr.append(x)

print(arr)

s = int(input("Enter value for search : "))

k = 0

for e in arr:
    if e == s:
        print(k)
        print(arr.index(s))
        break

else:
    print("Not found")