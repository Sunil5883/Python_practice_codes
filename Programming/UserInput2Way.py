li = input("Enter space seperated Elements") #--> input from user is 10 20 30 40
print(li, type(li)) # --> 10 20 30 40 <class 'str'>
li = li.split()
print(li) # --> ['10', '20', '30', '40']

li = list(map(int,li)) # --> [10, 20, 30, 40]
print(li)


tup = tuple(map(int,input("Enter Space sepearated elements ").split()))
print(tup) # --> (10, 20, 30)

li = list(map(int, input().split())) # --> 10 11 12 13
print([i for i in li if i %2 == 0]) # --> [10, 12]