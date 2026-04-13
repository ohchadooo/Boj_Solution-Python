def f(i):
  x=y=i
  for _ in range(ha(lth[i])):x=A[x]
  for _ in range(lth[i]):
    res[y-1]=x
    x=A[x];y=A[y];vis[y]=0

def ha(x):
  if x in sv:return sv[x]
  rep=0
  t=pow(10,sq,x)
  for p in rem:
    rep=(rep*t+p)%x
  sv[x]=rep
  return rep

n,m=input().split()
n=int(n)

A=[0]+[*map(int,input().split())]
vis=[0]*(n+1)
lth=[1]*(n+1)
for i in range(1,n+1):
  if vis[i]<1:
    x=i;c=1
    while i!=A[x]:x=A[x];c+=1;vis[x]=1
    vis[i]=1;lth[i]=c

k=len(m)
sq=int(k**0.5)

e=k%sq
rem=[int(m[:e])] if e else []
rem+=[int(m[i:i+sq])for i in range(e,k,sq)]

sv={}

res=[0]*n
for i in range(1,n+1):
  if vis[i]:f(i)

print(*res)
