s =input().split()
s1= 0
s2 = 0
c = 0
for i in s:
    s1 = i[::-1]
    s2 = str(s1).capitalize()
    if i == s1:
        c+=1
    elif i == s2:
        c+=1
print(c)