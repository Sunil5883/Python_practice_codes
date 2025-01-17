#Without input() and without return statement
def add():
    a = 10
    b = 20
    print('Addition of a and b', a+b)
add()

#With input() and without return statement
def sub(a,b):
    print('Subtraction:', a-b)

sub(10,5)

#Without input() and with return statement:
def mul():
    return 10 + 20

print(mul())

#With Input() and with return statement:
def div(a,b):
    return a/b

print(div(10,5))