import sys
input = sys.stdin.readline

n=int(input())
A=[*map(int,input().split())]

sq=int(n**0.5)
Q=[list(map(int,input().split()))+[i] for i in range(int(input()))]
Q.sort(key=lambda x:((x[0]-1)//sq,x[1]))

ans=[0]*len(Q)

dist=[0]*1000001
i=j=cnt=0
for a,b,id in Q:
  a-=1
  if i//sq!=a//sq:
    cnt=0
    dist=[0]*1000001
    for p in range((a//sq+1)*sq,b//sq*sq):
      if dist[A[p]]<1:cnt+=1;dist[A[p]]=1

  else:
    if j//sq<b//sq:
      x=max(j//sq,a//sq+1)*sq
      for p in range(x,b//sq*sq):
        if dist[A[p]]<1:cnt+=1;dist[A[p]]=1

  tcnt=0
  if a//sq!=b//sq:
    for p in range(a,(a//sq+1)*sq):
      if dist[A[p]]<1 and dist[A[p]]!=~id:
        tcnt+=1;dist[A[p]]=~id
    for p in range(b//sq*sq,b):
      if dist[A[p]]<1 and dist[A[p]]!=~id:
        tcnt+=1;dist[A[p]]=~id
  else:
    for p in range(a,b):
      if dist[A[p]]<1 and dist[A[p]]!=~id:
        tcnt+=1;dist[A[p]]=~id

  ans[id]=cnt+tcnt
  i,j=a,b

print(*ans)
