# d = {10:2, 20:1, 30:1}

# for num,count in d.items():
#     print(f"{num} occures {count} time(s)")

li = list(map(int,input().split()))
d = {}

for i in li:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

for num,count in d.items():
    print(f"{num} occures {count} time(s)")