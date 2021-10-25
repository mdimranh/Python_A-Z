a = [1, 2, 3, 4, 5, 6, 7]
b = [8, 9, 10, 11, 12, 13]

if len(a) == 2:
    print(f"{a[0]} and {a[1]}")

elif len(a) == 3:
    print(f"{a[0]}, {a[1]} and {a[2]}")

else:
    print("a = ", end="")
    for i in range(1, len(a)-1):
        print(f"{i}, ", end="")
    print(f"{a[-2]} and {a[-1]}")

c = a.copy()

c[0] = 100
print(f'Replace : {c}')

c.append(10)
print(f'Append : {c}')

c.insert(2, 10)
print(f'Insert in index of 2 : {c}')

c.reverse()
print(f'Reverse : {c}')

c.remove(10)
print(f'Remove : {c}')

c.pop(1)
print(f'Pop of index 1 : {c}')

a.extend(b)
print('Extend b with a : ', a)

c.sort()
print(f'Sorted c : {c}')