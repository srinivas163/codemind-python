n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
l1 = []
for i in range(n):
    if l[i]>=a and l[i]<=b:
        l1.append(l[i])
print(sum(l1))