class person:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

class student(person):
    def __init__(self, semister, section, name, id, email):
        super().__init__(name, id, email)
        self.section = section
        self.semister = semister

    def set_section(self, section):
        self.section = section
        if type(self.section) is int:
            print('Not a valid section')
            return
        return f"section = {self.section}"

    def summary(self):
        return f"name = {self.name}, section = {self.section}, semister = {self.semister}"

class teacher(person):
    def __init__(self, department, feature, name, id, email):
        super().__init__(name, id, email)
        self.department = department
        self.feature = feature

stdnt = student("12th", "PC-D", "Imran", '1984', 'imranh750')
x = stdnt.summary()
print(x)

print(stdnt.set_section('PC-E'))
