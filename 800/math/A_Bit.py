t=int(input())
x=0
for i in range(t):
    y=input()
    if y=="++X" or y=="X++":
        x+=1
    else:
        x-=1
print(x)