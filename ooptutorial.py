class person:
    def __init__(self, person_name: str, yob: int, height: float = None):
        self.__name = person_name
        self.__date_of_birth = yob
        self.__height = height

    def get_name(self):
        return self.__name

    def get_yob(self):
        return self.__date_of_birth

    def set_name(self, new_name):
        if (self.__has_any_number(new_name)):
            print("name is wrong")
            return
        self.__name = new_name

    def __has_any_number(self, string):
        return "0" in string

    def get_summary(self):
        pass
        # return f"Name : {self.__name}, DOB : {self.__date_of_birth}, Height: {self.__height if self.__height is not None else 'Invalid'}"


person_list = [person("Imran Hossain", 1998, 62),
               person("Mehedi", 1997),
               person("Sonet", 2000, 90),
               person("Kashfee", 1998)]

# for person in person_list:
#     if person.get_yob() >= 1998:
#         print(person.get_summary())


class Student(person):
    def __init__(self, person_name: str, yob: int, email : str, id : str):
        super().__init__(person_name, yob)
        self.email = email
        self.id = id

    def get_summary(self):
        return f"name : {self.get_name()}, Id : {self.id}, Email : {self.email}, yob : {self.get_yob()}"

    def __str__(self):
        return self.get_summary()

    def __repr__(self):
        return self.get_summary()


student = Student("Student", 2000, 'a@b.c', '1984')
print(student.get_summary())
student.set_name("Imran hossain")
print(student)


class Teacher(person):
    def __init__(self, person_name: str, yob: int, department: str):
        super().__init__(person_name, yob)
        self.dept = department

    def get_summary(self):
        return f"{self.get_name()} is a teacher."

new_person_list = [
    person("Imran", 1990),
    Student("Mehedi", 2000, "a@C.D", "Stid"),
    Teacher("Sonet", 1980, "cse")
]

for p in new_person_list:
    print(p.get_summary())


class plainclass:
    pass

abc = plainclass()
abc.age = 30
abc.name = "Movie"

print(abc.age)
