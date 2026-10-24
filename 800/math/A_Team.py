t=int(input())
d=0
for i in range(t):
    a,b,c=map(int,input().split())
    if a+b+c>1:
        d+=1
print(d)
