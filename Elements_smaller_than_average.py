n = int(input())
l = list(map(int,input().split()))
avg = sum(l)//len(l)
l1 = []
for i in range(n):
    if l[i]<=avg:
        l1.append(l[i])
print(len(l1))