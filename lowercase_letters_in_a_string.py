s = input()
a = "abcdefghijklmnopqrstuvwxyz"
l = []
for i in s:
    if i in a:
        l.append(i)
print(len(l))