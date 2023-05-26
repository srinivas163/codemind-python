n = int(input())
a = list(map(int,input().split()))
s =0
for i in range(n):
    if a[i]==0 or a[i]==1:
        a.sort()
        print(*a)
        break
