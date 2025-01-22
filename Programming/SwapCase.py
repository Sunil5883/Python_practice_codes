def swapcase(s):
    sample = ""
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        elif i.upper():
            sample = sample + i.lower()
        else:
            sample = sample + i
    return sample

print(swapcase("PythON"))