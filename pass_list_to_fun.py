def count(list):
    even = 0
    odd = 0

    for i in list:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even, odd


list = [1, 2, 3, 4, 5, 6]

even, odd = count(list)

print(f'even : {even} and odd : {odd}')