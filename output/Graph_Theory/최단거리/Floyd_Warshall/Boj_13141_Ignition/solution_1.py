import sys
input = sys.stdin.readline

n,m=map(int,input().split())
inf=10**18
dist=[[inf]*n for i in range(n)]

g=[]

for i in range(m):
  a,b,l=map(int,input().split())
  g.append((a-1,b-1,l))
  dist[a-1][b-1]=dist[b-1][a-1]=min(dist[a-1][b-1],l/1)

for i in range(n):dist[i][i]=0

for i in range(n):
  for j in range(n):
    for k in range(n):
      x=dist[j][i]+dist[i][k]
      if dist[j][k]>x:dist[j][k]=x

m=inf
for D in dist:
  M=0
  for a,b,l in g:
    if D[a]<D[b]:a,b=b,a
    M=max(M,D[a],D[a]+(l-D[a]+D[b])/2)
  m=min(m,M)

print(m)
