import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def f(u,p):
  global k,M
  dfo[u]=low[u]=k
  k+=1
  cuts=0 if p==-1 else 1
  for v in g[u]:
    if dfo[v]:
      if u!=p:low[u]=min(low[u],dfo[v])
      continue

    f(v,u)
    low[u]=min(low[v],low[u])
    if low[v]>=dfo[u]:cuts+=1

  if M<cuts:M=cuts


while (x:=tuple(map(int,input().split())))!=(0,0):
  n,s=x

  g=[[]for i in range(n)]
  for i in range(s):
    a,b=map(int,input().split())
    g[a]+=b,;g[b]+=a,

  dfo=[0]*n
  low=dfo[:]

  k=1;s=-1;M=0
  for i in range(n):
    if dfo[i]<1:
      s+=1
      f(i,-1)

  print(s+M)
