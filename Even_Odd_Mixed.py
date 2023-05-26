x = int(input())
s = 0
e = 0
o = 0
while x!=0:
    r = x%10
    s+=1
    if x%2==0:
        e+=1
    else:
        o+=1
    x = x//10
if s==e:
    print("Even")
elif s==o:
    print("Odd")
else:
    print("Mixed")