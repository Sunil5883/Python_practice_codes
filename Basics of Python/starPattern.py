row = 4
col = 5
for i in range(row):
    for j in range(col):
        print('*',end="")
    print()

print()
for i in range(row):
    for j in range(i+1):
        print('*',end="")
    print()

for i in range(row):
    for j in range((row)-i-1):
        print('*',end="")
    print()

for i in range(row):
    for j in range(i, row):
        print('*',end="")
    print()

