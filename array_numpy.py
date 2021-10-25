

'''array(), linspace(), logspace(), arange(), zeros(), ones()'''


from numpy import *

arr1 = array([1, 2, 3, 4, 5])  #int
arr2 = array([1, 2.5, 3, 4, 5])  #float for 2.5
arr3 = array([1, 2.5, '3', 4, 5])  #string for '3'

arr4 = array([1, 2, 3, 4, 5], int)
arr5 = array([1, 2, 3, 4, 5], float)
arr6 = array([1, 2, 3, 4, 5], str)

print(f"{arr4}, {arr5}, {arr6}")

arr7 = linspace(0, 16, 9) # number of 0 to 16, devided into 9 part
print(arr7)

arr8 = arange(1, 17, 3) # from previous number to next number the difference is 3
print(arr8)

arr9 = logspace(1, 40, 5) # its work for log which is come from math
print(arr9)

arr10 = zeros(5) # 5 time zero(0), in default it will float
print(arr10)

arr11 = ones(5) # 5 time one(1), in default it will float
print(arr11)