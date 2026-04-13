#boj 13548

import sys
input = sys.stdin.readline

n=int(input())
A=[*map(int,input().split())]
sq=int(n**0.5)

Q=[[*map(int,input().split())]+[_] for _ in range(int(input()))]
Q.sort(key=lambda x:((x[0]-1)//sq,x[1]))

ans=[0]*len(Q)
app=[0]*100001
i=j=cnt=0
for a,b,id in Q:
  a-=1
  if i//sq!=a//sq:
    cnt=0
    for p in range(i,j):app[A[p]]=0
    for p in range((a//sq+1)*sq,b):
      app[A[p]]+=1
      if app[A[p]]>cnt:cnt=app[A[p]]

  else:
    for p in range(max((a//sq+1)*sq,j),b):
      app[A[p]]+=1
      if app[A[p]]>cnt:cnt=app[A[p]]

  end=(a//sq+1)*sq if a//sq<b//sq else b
  tcnt=cnt

  for p in range(a,end):
    app[A[p]]+=1
    if app[A[p]]>tcnt:tcnt=app[A[p]]
  for p in range(a,end):app[A[p]]-=1

  ans[id]=tcnt

  i,j=a,b

print(*ans)
