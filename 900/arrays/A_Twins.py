t=int(input())
arr=list(map(int,input().split()))
arr.sort()
SUM=sum(arr)//2
u=0
c=0
for i in range(t-1,-1,-1):
    if u>SUM:
        break
    else:
        c+=1
        u+=arr[i]
print(c)

