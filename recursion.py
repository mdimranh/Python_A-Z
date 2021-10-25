
import sys

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

i = 0
def greet(i):
    i += 1
    print("Hello", i)
    greet(i)

greet(i)