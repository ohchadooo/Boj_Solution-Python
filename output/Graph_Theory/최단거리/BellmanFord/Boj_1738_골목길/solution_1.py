import sys
input = sys.stdin.readline

def dfs(x,a,ava):
  ava[x]=1
  for i,v in a[x]:
    if ava[i]:continue
    dfs(i,a,ava)

def bel():
  n,m=map(int,input().split())
  h=[[]for i in range(n+1)]
  for i in range(m):
    a,b,c=map(int,input().split())
    h[b]+=(a,c),

  av=[0]*(n+1)
  dfs(n,h,av)

  go=[]
  for i in range(1,n+1):
    if av[i]==0:continue
    for j,c in h[i]:
      if av[j]==0:continue
      go.append((j,i,c))

  inf=-10**8
  co=[inf]*(n+1);co[1]=0
  id=[0]*(n+1)

  for i in range(n):
    for a,b,c in go:
      if co[a]!=inf and co[b]<co[a]+c:
        co[b]=co[a]+c
        id[b]=a
        if i==n-1:return [-1]

  ans=[n]
  while ans[-1]>1:
    ans.append(id[ans[-1]])

  if ans[-1]==0:return [-1]
  return reversed(ans)

print(*bel())
