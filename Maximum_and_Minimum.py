n = int(input())
l = list(map(int,input().split()))
l1 = []
c = 0
for i in l:
    if l.count(i)==i and i not in l1:
        l1.append(i)
        c+=1
if c == 0:
    print("-1")
else:
    print(min(l1),max(l1),end = " ")