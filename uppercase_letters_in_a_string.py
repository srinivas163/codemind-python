s = input()
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l = []
for i in s:
    if i in a:
        l.append(i)
print(len(l))