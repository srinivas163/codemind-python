a = int(input())
b = 0
l = []
for i in range(1,a):
    if a%i==0:
        b+=i
if b == a:
    print(True)
else:
    print(False)