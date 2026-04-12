from heapq import *

v,e=map(int,input().split())
v+=1
k=int(input())

inf=1000000
note=[inf]*v
edge=[[]for i in range(v)]

vi=[0]*v

for i in range(e):
  a,b,c=map(int,input().split())
  edge[a]+=(b,c),

next=[(0,k)]
note[k]=0
while next:
  cost,cur=heappop(next)
  if vi[cur]:continue
  vi[cur]=1
  for i,w in edge[cur]:
    if cost+w<note[i]:
      note[i]=cost+w
      heappush(next,(cost+w,i))

for i in range(1,v):
  if note[i]==inf:print("INF")
  else:print(note[i])
