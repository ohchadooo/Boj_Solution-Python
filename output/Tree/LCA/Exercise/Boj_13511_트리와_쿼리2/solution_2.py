import sys
input = sys.stdin.readline

s=int(input())
n=s+1;k=0
while s:s>>=1;k+=1

g=[[]for i in range(n)]

for _ in range(n-2):
  u,v,w=map(int,input().split())
  g[u]+=(v,w),;g[v]+=(u,w),

P=[[0]*n for i in range(k)];P[0][1]=1,0
D=[0]*n
V=[0]*n

st=[1]
while st:
  i=st.pop()
  V[i]=1
  for j,w in g[i]:
    if V[j]:continue
    st+=j,
    D[j]=D[i]+1
    P[0][j]=i,w

for j in range(k-1):
  for i in range(1,n):
    a,b=P[j][i]
    c,d=P[j][a]
    P[j+1][i]=c,b+d

for _ in range(int(input())):
  a,b,c,*d=map(int,input().split())
  if d:d=d[0]

  T=0
  if D[b]<D[c]:T=1;b,c=c,b

  x,y=b,c #save

  w=0
  l=D[b]-D[c]
  for j in range(k):
    if l&(1<<j):
      w+=P[j][b][1]
      b=P[j][b][0]

  if b==c:lca=b
  else:
    for j in range(k-1,-1,-1):
      if P[j][b][0]!=P[j][c][0]:
        w+=P[j][b][1]+P[j][c][1]
        b=P[j][b][0];c=P[j][c][0]

    w+=P[0][b][1]+P[0][c][1]
    lca=P[0][b][0]

  if a==1:print(w)
  else:
    dx=D[x]-D[lca]
    dy=D[y]-D[lca]
    if T:
      d=dx+dy+2-d

    if d>dx+1:
      x=y
      d=dx+dy+1-d

    else:d-=1

    for j in range(k):
      if d&(1<<j):
        x=P[j][x][0]

    print(x)
