#메모리 절약
import sys
input = sys.stdin.readline

def f(i):
  global t
  while t<q and Q[t][0]==i:
    c,a,b,id=Q[t]
    x=dist[a-1][b-1]
    ans[id]=-1 if x==inf else x
    t+=1

n,q=map(int,input().split())
inf=10**18

dist=[[*map(int,input().split())]for i in range(n)]
for i in range(n):
  for j in range(n):
    if i!=j and dist[i][j]==0:dist[i][j]=inf

Q=[]
for i in range(q):Q.append([*map(int,input().split())]+[i])

Q.sort()
ans=[0]*q

t=0
for i in range(n):
  f(i+1)
  for j in range(n):
    for k in range(n):
      dist[j][k]=min(dist[j][k],dist[j][i]+dist[i][k])

f(n+1)
print(*ans)
