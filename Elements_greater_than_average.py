n = int(input())
l = list(map(int,input().split()))
avg = sum(l)//len(l)
c = 0
for i in range(n):
    if l[i]>=avg:
        c+=1
print(c)