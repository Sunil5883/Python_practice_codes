'''
1. In List we can store homogenous as well as Heterogenous Dat.
2. In List we can store the duplicate values.
3.List is an Ordered Collection of Data: Order of insertion will remain 
as it is in the Output.
4. Lists are Mutable: Once we declare the list we can modify it.
'''

lis1 = [10,20,30,40,'Sunil', True, 20]
print(lis1, type(lis1)) # [10, 20, 30, 40, 'Sunil', True, 20] <class 'list'>

'''append(value): this will add the given value in the list at last'''
lis1.append(100) 
print(lis1) # [10, 20, 30, 40, 'Sunil', True, 20, 100]

'''insert(index, value): inserts an value at the specified index in the value'''
lis1.insert(0, 5)
print(lis1) # [5, 10, 20, 30, 40, 'Sunil', True, 20, 100]

'''Removes the element first occurence of the specified data.'''
lis1.remove(10) 
print(lis1) # [5, 20, 30, 40, 'Sunil', True, 20, 100]

'''in and not in Operators: <Membership Operators>'''
print('Sunil' in lis1) # True
print(200 in lis1) # False

'''pop()
pop() without argumnent This will delete the last value and return the list'''
lis1.pop() # 100
print(lis1) # [5, 20, 30, 40, 'Sunil', True, 20]

'''pop(arguments) with arguments this will 
be delete the specified argument place int the list and return the re-arranged value'''
lis1.pop(1) # 10 will be removed
print(lis1) # [5, 30, 40, 'Sunil', True, 20]

'''del keyword:'''
del lis1[1] #this will remove the sepecified index values in the list
print(lis1) # [5, 40, 'Sunil', True, 20]

'''del lis1 this will delete entire list'''
del lis1
print(lis1) # this will delete the entire list 