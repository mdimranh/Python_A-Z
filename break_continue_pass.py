

'''
break = finish
continue = skip
pass = ignore
'''


av = 5
x = int(input("How manuy candies you want ? "))
i = 1
while i <= x:
    if i > av:
        print("Out of stock")
        break
    print("Candy", end=" ")
    i+=1
print()

for i in range(21):
    if i%3 == 0 or i%5 == 0:
        continue
    else:
        print(i, end=" ")
print()

for i in range(31):
    if i%3 == 0 and i%5 == 0:
        continue
    else:
        print(i, end=" ")

for i in range(21):
    if i%2 != 0:
        pass
    else:
        print(i, end=" ")