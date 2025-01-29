class Add:
    def calculate(self, a, b):
        print("Addition:", a + b)

class Sub:
    def calculate(self, a, b):
        print('Sub:', a - b)

class Mul:
    pass

def permit(ref, a,b):
    if type(ref).__name__ == 'Mul':
        print('Calculate is not possible in Mul')
    else:
        ref.calculate(a,b)

permit(Add(),10,20)
permit(Sub(),20,10)
permit(Mul(),10,20)

'''   
ref = Add()
ref.calculate(5,10) #15

ref = Sub()
ref.calculate(5,5) #0
'''