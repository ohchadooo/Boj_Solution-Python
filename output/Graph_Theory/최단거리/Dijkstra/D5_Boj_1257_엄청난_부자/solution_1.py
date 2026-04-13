from heapq import *

m=int(input())
n=int(input())

c=[*map(int,input().split())]
x=max(c)
c.remove(x)

graph=[[]for i in range(x)]
inf=10**5


dijk=[inf]*x
dijk[0]=0
next=[(0,0)]
vi=[0]*x

while next:
  cost,cur=heappop(next)
  if vi[cur]:continue
  vi[cur]=1
  for i in c:
    val=cost
    if cur+i<x:
      val+=1
    else:i-=x
    if val<dijk[cur+i]:
      dijk[cur+i]=val
      heappush(next,(val,cur+i))

a,b=divmod(m,x)
print(a+dijk[b])
