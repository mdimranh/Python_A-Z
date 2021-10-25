'''class car:
    def __init__(self, brand, colour, price):
        self.__brand = brand
        self.__colour = colour
        self.__price = price

    def get_brand(self):
        return self.__brand

    def set_colour(self, new_colour):
        if type(new_colour) is not str:
            print('Colour is invalid.')
            return
        self.__colour = new_colour

    def get_summary(self):
        return f"Brand : {self.__brand}, Colour : {self.__colour}, Price : {self.__price} "


car = car('BMW', 'Black', '$100M')
print(car.get_summary())
car.set_colour('White')
print(car.get_summary())'''


class person:
    def __init__(self, name, age, gndr):
        self.name = name
        if age is str:
            print("Not a valid age.")
        else:
            self.age = age
        self.gender = gndr

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.n_name = new_name
        if self.n_name is int:
            print("Please enter a valid name.")
            return
        self.name = new_name


    def get_summary(self):
        print(f"Name : {self.name}, age : {self.age}, gender : {self.gender}")


class teacher(person):
    def __init__(self, name, age, gndr, dept, feature):
        super().__init__(name, age, gndr)
        self.department = dept
        self.feature = feature

    def get_summary(self):
        return f"Name : {self.name}, Dept : {self.department}, Feature : {self.feature}"


class student(person):
    def __init__(self, name, age, gndr, dept, semister, sec):
        super().__init__(name, age, gndr)
        self.department = dept
        self.semister = semister
        self.section = sec

    def set_semister(self, semister):
        self.semister = semister
        if self.semister is not str:
            return 'Not a valid string'
        else:
            self.semister = semister

    def get_summary(self):
        return f"Name : {self.name}, dept : {self.department}, Semister : {self.semister}, Sec : {self.section}"


teacher = teacher("Imran", '22', "Male", "CSE", "Associate head")
print(teacher.get_summary())