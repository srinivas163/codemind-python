s = input()
a = []
l = []
for i in s:
    if i in 'aeiou':
        a.append(i)
for j in 'aeiou':
    if j not in a:
        l.append(j)
if len(l)==0:
    print('0')
else:
    print(*l)