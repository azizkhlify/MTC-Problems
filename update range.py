n,q=[int (x) for x in input().split()]
a=[int (x) for x in input().split()]
prefix=[0]*(n+1)
for i in range(q):
    l,r,v=[int (x) for x in input().split()]
    prefix[l-1]+=v
    prefix[r]-=v
for i in range(1,n+1):
    prefix[i]+=prefix[i-1]
for i in range(n):
    print(a[i]+prefix[i],end=" ")
