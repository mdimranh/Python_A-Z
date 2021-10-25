a = 10   # global variable
print(id(a))
b = 20   # global variable

def something():
    #global a
    a = 15         # local variable

    x = globals()['a']
    print(id(x))
    print('x', x)

    globals()['a'] = 9

    global c
    c = 30     # global function

    print('B in function ', b)
    print('A in function ', a)


something()
print('A, outside of function ', a)
print('C, outside of function ', c)
