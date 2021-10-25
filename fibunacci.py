
def fib(n):
    if n <= 0:
        print("Envalid input !!")
    else:
        fi1 = 0
        fi2 = 1
        for i in range(n):
            print(fi1)
            a = fi1
            fi1 = fi1+fi2
            fi2 = a


n = int(input('Enter value : '))
fib(n)