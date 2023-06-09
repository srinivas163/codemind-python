n = input().lower()
n = list(n)
l = []
for i in range(len(n)):
    if n[i]==" ":
        continue
    c = n.count(n[i])
    if c ==1:
        print(n[i])
        break
else:
    print("-1")