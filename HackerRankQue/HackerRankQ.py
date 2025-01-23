# li = list(map(int, input().split()))
li = [10,20,40,30,40]
li = list(set(li))
li.sort(reverse='True')
print(li)