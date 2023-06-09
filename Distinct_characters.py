s = input().lower()
s = list(s)
s.sort()
s1 = ""
for i in range(len(s)):
    if s[i]==" ":
        continue
    c= s.count(s[i])
    if c==1:
        s1+=s[i]
print(s1)