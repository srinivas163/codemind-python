a,b=map(int,input().split())
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)