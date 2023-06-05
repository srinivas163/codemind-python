s,t,b = map(int,input().split())
cap = 2*s*t*b*512
cpkb = cap//1024
print(cpkb,end = "KB")