r,c = map(int,input().split())
m = [list(map(int,input().split())) for i in range(r)]
l1 = []
for i in range(c):
    s = 0
    l = []
    for j in range(r):
        l.append(m[j][i])
        s = sum(l)
        l1.append(s)
print(max(l1))