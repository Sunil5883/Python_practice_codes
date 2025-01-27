class MathOperations:
    @staticmethod
    def addNumbers(a,b):
        return a + b
    def calci(self):
        pass
result = MathOperations.addNumbers(5,10)
print(f"By Calling using the class name {result}")

math_op = MathOperations()
print(f"This method is called by class instance variables {math_op.addNumbers(5,15)}")