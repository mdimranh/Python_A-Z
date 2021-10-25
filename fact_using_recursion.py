
# ==> Factorial


n = int(input("Enter a number : "))

def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)


result1 = fac(n)
print(f"fact : {result1}")



# ==> Summation



def sum(n):
    if n < 0:
        return 0
    return n+sum(n-1)

result2 = sum(n)
print(f"sum : {result2}")