dic = {}
n = int(input())
for i in range(n):
    name, *score = input().split()
    score = list(map(float, score))
    dic[name] = score
target_name = input()
avg = 0
for name, score in dic.items():
    if name == target_name:
        avg = sum(score)/len(score)
print(f"{avg:.2f}")
