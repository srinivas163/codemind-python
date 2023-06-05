n = int(input())
l = list(map(int,input().split()))
a,b = map(int,input().split())
s = 0
for i in range(n):
    if a>l[i] or b<l[i]:
        s+=l[i]
print(s)