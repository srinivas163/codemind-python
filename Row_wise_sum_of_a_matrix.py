r,c = map(int,input().split())
m = [list(map(int,input().split())) for i in range(r)]
l1 = []
for i in range(r):
    s = 0
    for j in range(c):
        s += m[i][j]
    l1.append(s)
print(*l1)