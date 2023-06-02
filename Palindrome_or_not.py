s = str(input())
s1 = s[::-1]
s2 = s1.capitalize()
if s == s1:
    print(True)
elif s == s2:
    print(True)
else:
    print(False)