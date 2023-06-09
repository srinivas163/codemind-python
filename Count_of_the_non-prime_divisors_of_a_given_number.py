import math
def pr(a):
    if a ==1:
        return False
    else:
        for i in range(2,int(math.sqrt(a))+1):
            if a%i==0:
                return False
        return True
m = int(input())
c = 0
for i in range(1,m+1):
    if m%i==0 and pr(i)==False:
        c+=1
print(c)