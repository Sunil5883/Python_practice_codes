def mutation(string, position, character):
    li = list(string)
    li[position] = character
    res = "".join(li)
    return res
print(mutation("Koknest",2,"d"))