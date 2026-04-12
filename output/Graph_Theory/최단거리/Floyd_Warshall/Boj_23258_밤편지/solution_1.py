import sys
input = sys.stdin.readline
def cop(A):return [i[:]for i in A]

n,q=map(int,input().split())
inf=10**18

dist=[[*map(int,input().split())]for i in range(n)]
for i in range(n):
  for j in range(n):
    if i!=j and dist[i][j]==0:dist[i][j]=inf

d2=[cop(dist)]

for i in range(n):
  for j in range(n):
    for k in range(n):
      dist[j][k]=min(dist[j][k],dist[j][i]+dist[i][k])
  d2.append(cop(dist))

for i in range(q):
  c,a,b=map(int,input().split())
  x=d2[c-1][a-1][b-1]
  print(-1 if x==inf else x)
