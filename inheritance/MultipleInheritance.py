class Demo1:
    def disp1(slef):
        print("Inside disp1")
class Demo2:
    def disp2(self):
        print("Inside disp2")
class Demo3(Demo1,Demo2):
    pass

d1 = Demo3()
d1.disp1()
d1.disp2()
