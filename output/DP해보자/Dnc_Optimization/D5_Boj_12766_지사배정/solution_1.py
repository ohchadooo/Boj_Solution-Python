from heapq import *

def dnc(s,e,p,q):
  m=(s+e)>>1

  opt=p
  mini=inf
  for i in range(p,min(m+1,q)):
    k=dp[i][x-1]+(m-i-1)*(S[m]-S[i])
    if k<mini:
      opt=i
      mini=k

  dp[m][x]=mini

  if s+2>e:return

  dnc(s,m,p,opt+1)
  dnc(m,e,opt,q)


n,b,s,r=map(int,input().split())
n+=1;b+=1

road=[[]for i in range(n)]
rev=[[]for i in range(n)]

for i in range(r):
  A,B,l=map(int,input().split())
  road[A].append((B,l))
  rev[B].append((A,l))

inf=10**18

fromhead=[inf]*n
tohead=[inf]*n

from_stack=[(0,b)]
to_stack=[(0,b)]

fromhead[b]=fromhead[0]=0
tohead[b]=tohead[0]=0

nvis=[0]*n

while from_stack:
  cost,cur=heappop(from_stack)
  if nvis[cur]:continue
  nvis[cur]=1
  for i,w in road[cur]:
    if w+cost<fromhead[i]:
      fromhead[i]=w+fromhead[cur]
      heappush(from_stack,(w+cost,i))

for i in range(n):nvis[i]=0

while to_stack:
  cost,cur=heappop(to_stack)
  if nvis[cur]:continue
  nvis[cur]=1
  for i,w in rev[cur]:
    if w+cost<tohead[i]:
      tohead[i]=w+tohead[cur]
      heappush(to_stack,(w+cost,i))

C=[fromhead[i]+tohead[i] for i in range(b)]
C.sort()

S=[0]
for i in range(1,b):
  S+=S[-1]+C[i],

dp=[[0]*s for i in range(b)]  #dp[g][i] g:count, i:1~i
for i in range(b):
  dp[i][0]=S[i]*(i-1)

for x in range(1,s):
  dnc(1,b,1,b)

print(dp[b-1][s-1])
