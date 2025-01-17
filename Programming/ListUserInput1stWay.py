li = []
num = int(input("Enter the number of elements to be entered: \n"))

for i in range(num):
    ele = int(input(f"Enter the element to be added: {i} \t"))
    li.append(ele)

print(li)
'''
Enter the number of elements to be entered: 
5
Enter the element to be added: 0        100
Enter the element to be added: 1        200
Enter the element to be added: 2        300
Enter the element to be added: 3        400
Enter the element to be added: 4        500
[100, 200, 300, 400, 500]
'''