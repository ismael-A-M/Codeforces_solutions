t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k={}
    d=0
    for j in range(n):
        key=a[j]-j
        if key in k:
            d+=k[key]
            k[key]+=1
        else:
            k[key]=1
    print(d) 