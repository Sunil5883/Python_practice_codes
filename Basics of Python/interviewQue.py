for y in range(1, 11):
    z = 200

def disp(a):
    print(a)
    y = 100
    print(y)

disp(50) #100
print(y) #200 the y is not defined in global but y is used in for loop so this y is used in outer loop also
# print(a) // error will get because we can't access the inside the local variables