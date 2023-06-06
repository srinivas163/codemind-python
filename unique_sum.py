n=int(input())
l=list(map(int,input().split()))
l1 = []
for i in range(n):
    if l[i] not in l1:
        l1.append(l[i])
print(sum(l1))