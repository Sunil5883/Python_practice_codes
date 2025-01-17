'''
In Tuple we can store Homogeneous as well as Heterogenous Data.
In Tuple we can store Duplicates.
Tuples are ordered COllection of Data.
Tuples are Immutable: Once we declare the tuple we cannot modify it.
'''

tup = (10, 22.55, 'Kodnest', True, 10)
print(tup, type(tup))

# del tup[1]
# print(tup)

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2 # Concatenation can be done in the tuple
print(t3)