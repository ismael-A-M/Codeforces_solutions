t=input()
c=1
ans="NO"
for i in range(len(t)-1):
    if t[i]==t[i+1]:
        c+=1
    else:
        c=1
    if c==7:
        ans="YES"
        break
print(ans)