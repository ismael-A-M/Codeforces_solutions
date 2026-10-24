t=int(input())
A=B=C=0
for i in range(t):
    a,b,c=map(int,input().split())
    A+=a
    B+=b
    C+=c
if A==B==C==0:
    print("YES")
else:
    print("NO")