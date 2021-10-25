class student:

    school = 'DIU' #class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1  #instance variable
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        return "this is student class.. in abc module"



s1 = student(74, 57, 32)
s2 = student(89, 32, 12)

print(s1.avg())
print(student.getSchool())
print(student.info())

