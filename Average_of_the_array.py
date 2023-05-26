n = int(input())
a = list(map(int,input().split()))
avg = sum(a)/len(a)
print("{:.2f}".format(avg))