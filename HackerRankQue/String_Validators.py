print('Kodnest1234*'.isalnum()) #False
print('Kodnest'.isalpha()) # True

print('Kodnest12'.isalpha()) # False
print('code'.isalpha())# True

print('12'.isdigit()) # True

#_________________LOGIC_____________________

s = input() #qA1
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))