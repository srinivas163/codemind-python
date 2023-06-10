s = input().lower().split()
s1 = input().lower().split()
c = 0
for i in s1:
    if i in s:
        c+=1
print(c)