import sys
input = sys.stdin.readline

n=int(input())
dist=[[*map(int,input().split())] for i in range(n)]
ch=[[1]*n for i in range(n)]

T=0
for i in range(n):
  for j in range(n):
    for k in range(n):
      if i==k or j==k:continue
      x=dist[i][k]+dist[k][j]
      if dist[i][j]==x:ch[i][j]=0;break
      elif x<dist[i][j]:T=1

if T:print(-1)
else:
  s=0
  for i in range(n):
    for j in range(n):
      s+=dist[i][j]*ch[i][j]
  print(s//2)
