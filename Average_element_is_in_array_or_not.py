n = int(input())
a = list(map(int,input().split()))
avg = sum(a)//len(a)
if avg in a:
    print(True)
else:
    print(False)