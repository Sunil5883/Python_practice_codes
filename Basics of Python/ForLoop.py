'''
for control_variable in range() or iterable_object
'''
# for i in 'Sunil':
#     print(i)

# for j in [10,15,20]:
#     print(j+5)

'''this below is considered as 1st argument as start and
last argument as last-1 '''
# for k in range(1,11):
#     print(k)

'''This below is considered as range(11,21,2) 
this will take the first argument as start and 2nd argument wil
be take as last-1 and third argument is increase the value by 2steps'''
# for m in range(11,21,2):
#     print(m)

# print()

'''This below considered as range(5) 
is till the end and the starting number is 0
'''
# for i in range(5):
#     print(i,end=' ')

for i in range(1,11):
    if(i == 6):
        continue
    else:
        print(i)
print()

for j in range(1,11):
    if(j == 5):
        break
    else:
        print(j)

def disp():
    pass

class Demo:
    pass
