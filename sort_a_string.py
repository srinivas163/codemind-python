s = input()
s1 = []
for i in s:
    if i.isalnum():
        s1.append(i)
s1.sort()
a = 0
for i in s:
    if i.isalnum():
        print(s1[a],end = "")
        a+=1
    else:
        print(i,end= "")