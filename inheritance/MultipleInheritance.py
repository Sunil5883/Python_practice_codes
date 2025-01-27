class Demo1:
    def disp1(self):
        print("Inside disp1")
class Demo2(Demo1):
    def dips2(self):
        print("Inside disp2")
class Demo3(Demo2):
    def disp3(self):
        print("Inside disp3")

d3 = Demo3()
d3.disp1()
d3.dips2()
d3.disp3()