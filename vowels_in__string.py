s = input()
k = []
for i in s:
    if i in 'aeiouAEIOU' and i not in k:
        k.append(i)
print(*k)