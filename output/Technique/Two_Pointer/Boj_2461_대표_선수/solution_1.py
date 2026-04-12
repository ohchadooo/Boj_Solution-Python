import sys
input=sys.stdin.readline
from heapq import *

n,k=map(int,input().split())
a=[sorted(map(int,input().split()))for i in range(n)]

id=[0]*n
m=10**9

x=[(a[i][0],i)for i in range(n)]
heapify(x)
M=max(i[0]for i in a)
while 1:
  t,i=heappop(x)
  m=min(m,M-t)
  id[i]+=1
  if id[i]==k:break
  y=a[i][id[i]]
  heappush(x,(y,i))
  if y>M:M=y

print(m)
