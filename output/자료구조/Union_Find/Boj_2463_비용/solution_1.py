def union(x,y,w):
  global cost,save
  a,b=find(x),find(y)
  if a==b:
    cost=(cost+save*w)%mod
    return
  if p[a]>p[b]:b,a=a,b
  save+=p[a]*p[b]
  p[a]+=p[b]
  p[b]=a
  cost=(cost+save*w)%mod

def find(x):
  if p[x]<0:return x
  p[x]=find(p[x])
  return p[x]

n,m=map(int,input().split())
mod=10**9

a=[[*map(int,input().split())] for i in range(m)]
a.sort(key=lambda x:-x[2])

p=[-1]*(n+1)

cost=save=0
for i in a:union(*i)

print(cost)
