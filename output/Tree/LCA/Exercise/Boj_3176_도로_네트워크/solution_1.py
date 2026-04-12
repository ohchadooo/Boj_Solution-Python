import sys
input = sys.stdin.readline

def sol():
  n=int(input())+1
  INF=1000000

  s=n-1;k=0
  while s:s>>=1;k+=1

  g=[[]for i in range(n)]
  for i in range(n-2):
    a,b,c=map(int,input().split())
    g[a].append((b,c));g[b].append((a,c))

  P=[[0]*n for i in range(k)];P[0][1]=1
  mn=[[INF]*n for i in range(k)]
  mx=[[0]*n for i in range(k)]

  D=[0]*n

  st=[1]
  while st:
    i=st.pop()
    for j,c in g[i]:
      if P[0][i]==j:continue
      st.append(j)
      D[j]=D[i]+1
      P[0][j]=i
      mn[0][j]=c
      mx[0][j]=c

  for j in range(k-1):
    Pj=P[j];Pj1=P[j+1]
    mnj=mn[j];mnj1=mn[j+1]
    mxj=mx[j];mxj1=mx[j+1]
    for i in range(1,n):
      y=Pj[i]
      Pj1[i]=Pj[y]
      mnj1[i]=min(mnj[i],mnj[y])
      mxj1[i]=max(mxj[i],mxj[y])

  for _ in range(int(input())):
    d,e=map(int,input().split())
    m=INF;M=0

    if D[d]<D[e]:d,e=e,d
    l=D[d]-D[e]

    for j in range(k):
      if l&(1<<j):
        if mn[j][d]<m:m=mn[j][d]
        if mx[j][d]>M:M=mx[j][d]
        d=P[j][d]


    if d==e:print(m,M);continue

    for j in range(k-1,-1,-1):
      if P[j][d]!=P[j][e]:
        if mn[j][d]<m:m=mn[j][d]
        if mn[j][e]<m:m=mn[j][e]
        if mx[j][d]>M:M=mx[j][d]
        if mx[j][e]>M:M=mx[j][e]
        d=P[j][d];e=P[j][e]

    if mn[0][d]<m:m=mn[0][d]
    if mn[0][e]<m:m=mn[0][e]
    if mx[0][d]>M:M=mx[0][d]
    if mx[0][e]>M:M=mx[0][e]

    print(m,M)

sol()
