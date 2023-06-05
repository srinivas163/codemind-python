n = int(input())
l = list(map(int,input().split()))
l1 = []
for i in range(n):
    if l[i]%2==0:
        l1.append(l[i])
for i in range(n):
    if l[i]%2!=0:
        l1.append(l[i])
print(*l1)