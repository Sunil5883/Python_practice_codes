'''
reverse() will reverse the original object
'''
li = [10,20,30,40]
print(li) # [10, 20, 30, 40]

li2 = li.reverse()
print("After Reverse:", li) # After Reverse: [40, 30, 20, 10]

print(li) # [40, 30, 20, 10]

'''
list(reversed(object)): if print like this-->(revresed(object)) <--this will be give some iterable_object
so  to overCome the print we need to give this --> (list(reversed(obj)));
'''

li3= [11,22,33,44]
print(li3)

print(list(reversed(li3)))
print(li3)

li4 = [1,5,2,9]
new_reverse_li4 = list(reversed(li4)) # --> this will create new list as reversed
li4.reverse() #---> Reveresing Original list