x,y,m = map(int,input().split())
a =1
for i in range(y):
    a = a*x
print(a%m)