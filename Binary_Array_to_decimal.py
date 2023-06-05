n = int(input())
l = list(map(int,input().split()))
s = 0
for i in range(n):
    n-=1
    s=s+(l[i]*2**n)
print(s)