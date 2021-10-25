from numpy import *

arr1 = array([1, 2, 3, 4])
print(arr1+1)
arr2 = array([1, 2, 3, 4])

arr = arr1 + arr2       # vectorized operation

print(arr)

print(concatenate([arr1, arr2]))

print(sin(arr))
print(log(arr))
print(sqrt(arr))


''' ==> shallow copy <== '''


arr3 = array([1, 3, 5, 7])

arr4 = arr3.view()

arr3[1] = 4

print("==> shallow copy <==")

print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))


''' ==> deep copy <== '''

arr5 = array([1, 3, 5, 7])

arr6 = arr5.copy()

arr5[1] = 4

print("==> deep copy <==")

print(arr5)
print(arr6)

print(id(arr5))
print(id(arr6))

