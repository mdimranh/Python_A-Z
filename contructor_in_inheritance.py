class A:

    def __init__(self):
        print("In 'A' init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):

    def __init__(self):
        print("In 'B' init" )

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A):

    def feature5(self):
        print("Feature 5 working")

    def feature6(self):
        print("Feature 6 working")

class D(A):

    def __init__(self):
        super().__init__()
        print("In 'D' init")

    def feature7(self):
        print("Feature 5 working")

    def feature8(self):
        print("Feature 6 working")

class E:

    def __init__(self):
        print("In 'E' init")

class F(A, E):

    def __init__(self):
        super().__init__()
        print("In 'F' init")

a1 = B()
a2 = C()
print('----------')
a3 = D()
print("----------")
a4 = F()