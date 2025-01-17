# if String is holding an integer value it can convert it as show below
a = '30'
print(a, type(a))
b = int(a)
print(b, type(b))

# String to int convertion is not allowed
x = 'Kod'
print(x, type(x))

y=int(x)
print(y, type(y))

float()
p = float(input('Enter the float type data'))
print(p, type(p))

# bool()
# (in bool() data type if the varaibles contains any type of data then it is
# give true)
# else the variable does not contain any data
# or '0' this data type will give false

r = 'Str'
print(r, type(r))
s = bool(r)

print(s,type(s))

print(int(12.22))