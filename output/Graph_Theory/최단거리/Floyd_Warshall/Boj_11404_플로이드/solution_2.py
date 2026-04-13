## boj 11780 플로이드 2

import sys
input = sys.stdin.readline

def track(i,j):
  k=bef[i][j]
  if k==i:return [i+1]

  return track(i,k)+track(k,j)

n=int(input())

inf=10**18
dist=[[inf]*n for i in range(n)]
bef=[[i for j in range(n)] for i in range(n)]

for i in range(n):dist[i][i]=0

for i in range(int(input())):
  a,b,w=map(int,input().split())
  dist[a-1][b-1]=dist[b-1][a-1]=min(dist[a-1][b-1],w)

for i in range(n):
  for j in range(n):
    for k in range(n):
      x=dist[j][i]+dist[i][k]
      if dist[j][k]>x:
        dist[j][k]=x
        bef[j][k]=i

for i in dist:
  for j in range(n):
    if i[j]==inf:i[j]=0
  print(*i)

for i in range(n):
  for j in range(n):
    if dist[i][j]==0:print(0);continue
    x=track(i,j)+[j+1]
    print(len(x),*x)
