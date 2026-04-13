import sys
input=sys.stdin.readline

n=int(input())

inf=10**18
dist=[[inf]*n for i in range(n)]

for i in range(n):dist[i][i]=0

for i in range(int(input())):
  a,b,w=map(int,input().split())
  dist[a-1][b-1]=dist[b-1][a-1]=min(dist[a-1][b-1],w)

for i in range(n):
  for j in range(n):
    for k in range(n):
      if dist[j][i]==inf or dist[i][k]==inf:continue #음수 간선 있을 때 필수
      dist[j][k]=min(dist[j][i]+dist[i][k],dist[j][k])

for i in dist:
  for j in range(n):
    if i[j]==inf:i[j]=0
  print(*i)
