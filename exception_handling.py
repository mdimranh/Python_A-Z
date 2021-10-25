a = 5
b = 2


try:
    print('Resource o pen')
    div = a/b
    print(div)
    k = int(input('Enter a number : '))
    print(k)

except ZeroDivisionError as e:
    print("You can't divide a number by zero", e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong", e)

finally:
    print('Resource closed')