s = input()
o = 'aeiouAEIOU'
c = 0
for i in s:
    if i in o:
        c+=1
if c==0:
    print("0")
else:
    print(c)