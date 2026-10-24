t=int(input())
arr=list(map(int,input().split()))
c=1
mx=1
for i in range(t-1):
    if arr[i]<=arr[i+1]:
        c+=1
    else:
        c=1
    mx=max(mx,c)
print(mx)
    