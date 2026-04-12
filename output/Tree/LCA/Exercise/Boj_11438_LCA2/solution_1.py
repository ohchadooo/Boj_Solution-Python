n=int(input())+1

s=n-1
k=0
while s:s>>=1;k+=1

g=[[]for i in range(n)]
for i in range(n-2):
  a,b=map(int,input().split())
  g[a].append(b);g[b].append(a)


vis=[0]*n
p=[[0]*n for i in range(k)]
d=[0]*n;d[1]=0

st=[1]
while st:
  i=st.pop()
  vis[i]=1
  di=d[i]
  for j in g[i]:
    if vis[j]:continue
    vis[j]=1
    d[j]=di+1
    p[0][j]=i
    st.append(j)

for l in range(k-1):
  for j in range(1,n):
    p[l+1][j]=p[l][p[l][j]]

m=int(input())

for _ in range(m):
  a,b=map(int,input().split())
  if d[a]>d[b]:
    x=d[a]-d[b]
    for i in range(k):
      if x&(1<<i):a=p[i][a]
  else:
    x=d[b]-d[a]
    for i in range(k):
      if x&(1<<i):b=p[i][b]

  if a==b:print(a);continue

  for i in range(k-1,-1,-1):
    if p[i][a]!=p[i][b]:
      a=p[i][a];b=p[i][b]

  print(p[0][a])
