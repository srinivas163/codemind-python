r,c = map(int,input().split())
m = [list(map(int,input().split())) for i in range(r)]
l1 = []
for i in range(r):
    s = 0
    l = []
    for j in range(c):
        l.append(m[i][j])
        s = sum(l)
        l1.append(s)
print(max(l1))