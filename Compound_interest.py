a,b,c = map(int,input().split())
i = a*(1+(b/100))**c
print("{:.2f}".format(i))