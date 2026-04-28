import collections
t=int(input())
l=[]
for i in range(t):
    n=input()
    l.append(n)
ar=collections.Counter(l)
print(max(ar, key=ar.get))