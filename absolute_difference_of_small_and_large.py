s = input().split()
for i in s:
    x = ord(max(i))
    y = ord(min(i))
    print(abs(x-y),end = " ")