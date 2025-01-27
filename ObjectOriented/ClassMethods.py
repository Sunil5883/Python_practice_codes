class Student:
    college = 'Kodnest'

    def get_info(self):
        print("College Name is :", Student.college)
    @classmethod
    def changeName(cls, newName):
        cls.college = newName

s1 = Student()
s1.get_info()
s1.changeName("Sunil's College")
s1.get_info()
