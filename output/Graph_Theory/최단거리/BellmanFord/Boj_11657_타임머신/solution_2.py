import sys
input = sys.stdin.readline

n,m=map(int,input().split())
g=[tuple(map(int,input().split())) for _ in range(m)]

inf=10**18
cost=[inf]*(n+1)

T=cost[1]=0
for i in range(n):
  nup=1
  for a,b,c in g:
    if cost[a]!=inf and cost[b]>cost[a]+c:
      cost[b]=cost[a]+c
      if i==n-1:T=1;break
      nup=0
  if nup:break

if T:print(-1)
else:
  for i in range(2,n+1):
    if cost[i]==inf:print(-1)
    else:print(cost[i])
