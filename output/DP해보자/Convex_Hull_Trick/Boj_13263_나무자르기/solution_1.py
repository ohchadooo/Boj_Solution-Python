from bisect import bisect_left as L

n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]

dp=[0]*n
junction=[0]
index=[0]

y=0

for i in range(1,n):
  id=index[L(junction,a[i])-1]
  dp[i]=b[id]*a[i]+dp[id]

  c=(dp[i]-dp[i-1])/(b[i-1]-b[i])
  while c<=junction[-1]:
    junction.pop();index.pop()
    j=index[-1]
    c=(dp[i]-dp[j])/(b[j]-b[i])

  junction+=c,
  index+=i,

print(dp[-1])
