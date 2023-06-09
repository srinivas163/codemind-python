n = input().lower()
n = list(n)
n.sort()
c = 0
for i in range(len(n)):
    if n[i]==" ":
        continue
    s = n.count(n[i])
    if s==1:
        c+=1
print(c)