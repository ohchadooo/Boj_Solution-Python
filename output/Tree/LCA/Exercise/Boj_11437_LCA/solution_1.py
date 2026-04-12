# Binary Lifting을 사용하지 않음

n=int(input())+1

g=[[]for i in range(n)]
for i in range(n-2):
  a,b=map(int,input().split())
  g[a]+=b,;g[b]+=a,

vis=[0]*n
p=[0]*n
d=[0]*n;d[1]=0

st=[1]
while st:
  i=st.pop()
  vis[i]=1
  for j in g[i]:
    if vis[j]:continue
    vis[j]=1
    d[j]=d[i]+1
    p[j]=i
    st.append(j)

m=int(input())

for _ in range(m):
  a,b=map(int,input().split())
  while d[a]>d[b]:a=p[a]
  while d[a]<d[b]:b=p[b]

  while a!=b:
    a=p[a];b=p[b]

  print(a)
