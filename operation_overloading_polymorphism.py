
a = 5
b = 6

print(a+b)
print(int.__add__(a,b))

print("-----------")

a = '5'
b = '6'

print(a+b)
print(str.__add__(a,b))
print("-----------")

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return self.m1, self.m2

s1 = student(58, 56)
s2 = student(88, 46)

s3 = s1+s2

if s1 > s2:
    print("S1 Wins")
else:
    print("S2 wins")


a = 9
print(a.__str__())

print(s1.__str__())