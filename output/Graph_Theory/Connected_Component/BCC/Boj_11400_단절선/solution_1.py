import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(u,p):
  global k
  dfo[u]=low[u]=k
  k+=1
  for v in g[u]:
    if dfo[v]:
      if v!=p:low[u]=min(low[u],dfo[v])
      continue

    dfs(v,u)
    low[u]=min(low[v],low[u])
    if low[v]>dfo[u]:
      bridge.append(sorted([u,v]))

n,e=map(int,input().split())
n+=1

g=[[]for i in range(n)]
for i in range(e):
  a,b=map(int,input().split())
  g[a]+=b,;g[b]+=a,

dfo=[0]*n
low=dfo[:]
bridge=[]

k=1
for i in range(1,n):
  if dfo[i]==0:dfs(i,-1)

bridge.sort()
print(len(bridge))
for i in bridge:print(*i)
