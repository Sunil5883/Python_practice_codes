rows = 4
col = 5

for i in range(rows):
    for j in range(i+1):
        print('*', end='')
    for k in range(i, rows-1):
        print(" ", end='')
    for k in range(i, rows-1):
        print(" ", end='')
    for j in range(i+1):
        print('*', end='')
    print()

for i in range(rows):
    for j in range(i, rows-1):
        print('*', end='')
    for k in range((i+1)):
        print(" ", end="")
    for k in range((i+1)):
        print(' ', end="")
    for k in range(i, rows-1):
        print("*", end='')
    print()