# map (function, iterable_object) ---> Iterable_object:

def double(x):
    return x*2

li = [1,2,3,4]
double_li = list(map(double, li))
print(double_li)

tup = ('10', '20', '30', '40')
print(tup) # --> ('10', '20', '30', '40')
tup2 = tuple(map(int, tup)) # --> (10, 20, 30, 40)
print(tup2)

li2 = [1,5,66]
print(li2) # --> [1,5,66]
li2_copy = list(map(float, li2)) # --> [1.0, 5.0, 66.0]
print(li2_copy)

li3 = [22.2,33.3,44.4]
print(li3) # --> [22.2,33.3,44.4]
li3_copy = list(map(int, li3)) # --> [22, 33, 44]
print(li3_copy)