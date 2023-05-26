n = int(input())
sq = pow(n,2)
mod = pow(10,len(str(n)))
if sq%mod==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")