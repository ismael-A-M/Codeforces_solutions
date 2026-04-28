t=int(input())
s={}
for i in range(t):
    n=input()
    if n in s:
        s[n]+=1
        print(n+f'{s[n]}')
    else:
        s[n]=0
        print("OK")