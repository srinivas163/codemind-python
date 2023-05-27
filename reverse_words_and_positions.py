def rev(n):
    return n[::-1]
n = input()
l = list(n.split(" "))
li = l[::-1]
for i in li:
    print(rev(n),end = " ")
    break