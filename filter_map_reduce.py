from functools import reduce

nums = [2, 4, 6, 5, 7, 8, 9, 3]

even = list(filter(lambda n : n%2 == 0, nums)) # filter only work for true and false

doubles = list(map(lambda n : n*2, even)) # map works for calculation

sum = reduce(lambda a, b : a+b, doubles)

print(even)
print(doubles)
print(sum)