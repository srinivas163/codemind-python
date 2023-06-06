n=input()
c=0
for i in n:
    if i.isalpha():
        c+=1
print(len(n)-c)