import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v,p):
  global k
  dfo[v]=low[v]=k
  k+=1
  ch=0

  for u in g[v]:
    if dfo[u]:
      if u!=p and low[v]>dfo[u]:low[v]=dfo[u]
      continue

    dfs(u,v)
    ch+=1
    if low[v]>low[u]:low[v]=low[u]

    if low[u]>=dfo[v]:
      if p!=-1:cut[v]=1

  if p==-1 and ch>1:cut[v]=1


n,e=map(int,input().split())
n+=1

g=[[] for i in range(n)]
for i in range(e):
  a,b=map(int,input().split())
  g[a]+=b,;g[b]+=a,

cut=[0]*n
dfo=cut[:]
low=cut[:]

k=1
for i in range(1,n):
  if dfo[i]==0:dfs(i,-1)

ans=[]
for i in range(1,n):
  if cut[i]:ans+=i,

print(len(ans),*ans)
