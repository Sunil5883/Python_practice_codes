class Demo:
    def disp(self):
        print("Inside disp with 0 para")
    def disp(self, a):
        print('Inside disp with 1 para')
    def disp(self,a,b):
        print("Inside disp with 2 para")

d1 = Demo()
# d1.disp()
# d1.disp(10)
d1.disp(5,10)