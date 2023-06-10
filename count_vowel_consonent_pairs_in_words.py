n = input().lower().split()
v = "aeiou"
c= 0
for i in n:
    for j in range(0,len(i)//2):
        if i[j] in v and i[-(j+1)] not in v or i[j] not in v and i[-(j+1)] in v:
            c+=1
print(c)