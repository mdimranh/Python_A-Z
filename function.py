def add(a, total):
    total = total+a
    return total

total = 0
number = int(input("How many number you want add ? "))
for i in range(number):
    a = int(input(f"Enter {i+1} number : "))
    add(a, total)
    total = add(a, total)
print (f"Total = {total}")