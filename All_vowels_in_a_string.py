s = input()
o = 'aeiou'
l = []
for i in s:
    if i in o and i not in l:
        l.append(i)
if len(l)==len(o):
    print(True)
else:
    print(False)