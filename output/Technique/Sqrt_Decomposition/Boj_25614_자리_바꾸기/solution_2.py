def f(i):
  x=y=i
  for _ in range(ha(lth[i])):x=A[x]
  for _ in range(lth[i]):
    res[y]=x
    x=A[x];y=A[y];vis[y]=0

def ha(x):
  if x in sv:return sv[x]
  sv[x]=m%x
  return sv[x]

n,m=map(int,input().split())
A=[0]+[*map(int,input().split())]
vis=[0]*(n+1)
lth=[1]*(n+1)
for i in range(1,n+1):
  if vis[i]<1:
    x=i
    c=1
    while i!=A[x]:x=A[x];c+=1;vis[x]=1
    vis[i]=1;lth[i]=c

sv={}

res=[0]*(n+1)
for i in range(1,n+1):
  if vis[i]:f(i)

print(*res[1:])
