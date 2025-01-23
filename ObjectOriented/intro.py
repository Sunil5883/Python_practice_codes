class Student:
    def learn(self):
        print(f'{self.name} Learn Method')
    def play():
        print('Inside Play Method')

s1 = Student()
s1.name = 'Sunil'
print('Name is', s1.name)
s1.learn()
# s1.play() # TypeError: Student.play() takes 0 positional arguments but 1 was given