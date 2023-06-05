s = input().split()
o = "aeiou"
l =[]
for i in s:
    c =0
    for j in i:
        if j in o:
            c+=1
    l.append(c)
print(l.count(min(l)))