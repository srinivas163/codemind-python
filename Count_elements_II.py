n,m=map(int,input().split())
l=list(map(int,input().split()))
ll=list(map(int,input().split()))
a=[]
for i in ll:
    if i not in l and i not in a:
            a.append(i)
for i in l:
    if i not in ll and i not in a:
            a.append(i)
print(len(a))