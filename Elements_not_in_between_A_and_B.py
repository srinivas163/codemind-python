n = int(input())
l = list(map(int,input().split()))
a,b = map(int,input().split())
l1 = []
for i in range(n):
    if a>l[i] or b<l[i]:
        l1.append(l[i])
if len(l1)==0:
    print("-1")
else:
    print(*l1)