a,b = map(int,input().split())
l = list(map(int,input().split()))
l1 = []
for i in l:
    if i%b==0:
        l1.append(i)
print(len(l1))