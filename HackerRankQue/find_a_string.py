main_s = input()
sub_s = input()
def count_substring(main_s, sub_s):
    n = len(main_s)-len(sub_s)+1
    count = 0
    for i in range(n):
        if (sub_s == main_s[i:i+len(sub_s)]):
            count+=1
    return count
count = count_substring(main_s,sub_s)
print(count)