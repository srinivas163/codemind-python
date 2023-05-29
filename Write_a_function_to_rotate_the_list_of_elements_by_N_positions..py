n = int(input())
l = list(map(int,input().split()))
r = int(input())
l1 = len(l)-1
for i in range(r):
    f = l[l1]
    for j in range(l1,-1,-1):
        l[j] = l[j-1]
    l[0] = f
print(*l)