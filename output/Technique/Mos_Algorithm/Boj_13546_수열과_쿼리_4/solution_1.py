import sys
input=sys.stdin.readline
from bisect import bisect as R,bisect_left as L

n,k=map(int,input().split())
sq=int(n**0.5)

A=[*map(int,input().split())]
Q=[[*map(int,input().split())]+[i] for i in range(int(input()))]
Q.sort(key=lambda x:((x[0]-1)//sq,x[1]))

pos=[[]for i in range(2*k+1)]
for i in range(n):pos[A[i]].append(i)

i=j=long=0
ans=[0]*len(Q)

for a,b,id in Q:
  a-=1
  if a//sq==b//sq:
    for p in range(a,b):
      target=pos[A[p]]
      x=target[R(target,b-1)-1]-p
      if x>ans[id]:ans[id]=x
    continue

  if i//sq!=a//sq:
    long=0
    for p in range((a//sq+1)*sq,b):
      target=pos[A[p]]
      x=target[R(target,b-1)-1]-p
      if x>long:long=x
  else:
    s=(a//sq+1)*sq
    for p in range(max(s,j),b):
      target=pos[A[p]]
      x=p-target[L(target,s)]
      if x>long:long=x

  ans[id]=long
  for p in range(a,(a//sq+1)*sq):
    target=pos[A[p]]
    x=target[R(target,b-1)-1]-p
    if x>ans[id]:ans[id]=x

  i,j=a,b

print(*ans)
