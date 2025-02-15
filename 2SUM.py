n,target=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
a.sort()
i=0
j=n-1
while i<j : 
    if a[i] + a[j] == target :
      print(a[i],a[j])
      exit(0)
    elif a[i]+a[j] < target : 
      i+=1
    else : 
      j-=1
print(-1)
