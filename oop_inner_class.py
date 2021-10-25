class student:

    def __init__(self, name, rollno):
        self.name = name
        self.roll = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class laptop:    #inner class

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student("Imran", 1)
s2 = student("Sonet", 2)

s1.show()
