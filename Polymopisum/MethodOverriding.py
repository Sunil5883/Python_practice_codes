class Calculator:
    def calculate(self,a,b):
       pass

class Add(Calculator):
    def calculate(self, a,b):
        print('Addition:', a + b)

class Sub(Calculator):
    def calculate(self, a, b):
        print('Sub:',a - b)

class Mul(Calculator):
    def calculate(self, a, b):
        print('Mul:', a * b)

'''def permit(ref,a,b):
    if type(ref).__name__ == 'Mul':
        print('There is no method to calculate')
    else:
        ref.calculate(a,b)
'''
ref = Add()
ref.calculate(10,20)

ref = Sub()
ref.calculate(20,10)

ref = Mul()
ref.calculate(10,2)
'''permit(Add(),5,15)
permit(Sub(), 20,10)
permit(Mul(),10,20)'''
