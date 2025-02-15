k = int(input())
nums = [int(x) for x in input().split()]
n = len(nums)
r = 0
s = 0
# Calcule de la somme de premier k-element
while (r<k):
    s+=nums[r]
    r+=1
res = s

for l in range(1, n-k+1):
    s+=nums[r]-nums[l-1]
    r+=1
    res = max(s, res)
print(res/k)
