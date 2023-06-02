r,c = map(int,input().split())
m = [list(map(int,input().split())) for i in range(r)]
l1 = []
for i in range(c):
    s = 0
    for j in range(r):
        s += m[j][i]
    l1.append(s)
print(*l1)