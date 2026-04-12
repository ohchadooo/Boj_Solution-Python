# Using RMQ

import sys
sys.setrecursionlimit(100000)

n=int(input())+1

g=[[]for i in range(n)]
for i in range(n-2):
  a,b=map(int,input().split())
  g[a]+=b,;g[b]+=a,

E=[];D=[]
nv=[1]*n

def dfs(x=1,c=0):  # 방문할 때, 돌아올 때 모두 저장
  global E,D
  E+=x,;D+=c,
  nv[x]=0
  for i in g[x]:
    if nv[i]:
      dfs(i,c+1)
      E+=x,;D+=c,

dfs()

N=len(E)
s=N-1;k=0
while s:s>>=1;k+=1

F=[0]*n
for i in range(N-1,-1,-1):
  F[E[i]]=i

rmq=[[i]*k for i in range(N)]

# u->...->lca->...->v
# lca=rmq(u,v)

for j in range(k-1):
  x=1<<j
  for i in range(N-1,0,-1):
    if i+x<N and D[rmq[i][j]]>D[rmq[i+x][j]]:
      rmq[i][j+1]=rmq[i+x][j]
    else:rmq[i][j+1]=rmq[i][j]

for _ in range(int(input())):
  a,b=map(int,input().split())
  x,y=F[a],F[b]
  if x>y:x,y=y,x

  l=y-x+1;t=-1
  while l:l>>=1;t+=1   # 길이보다 작은 최대의 2^k

  p=rmq[x][t];q=rmq[y-(1<<t)+1][t]
  print(E[p] if D[p]<D[q] else E[q])
