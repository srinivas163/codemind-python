n = input().lower()
n = list(n)
l = []
for i in n:
    if i not in l:
        l.append(i)
if " " in l:
    print(len(l)-1)
else:
    print(len(l))