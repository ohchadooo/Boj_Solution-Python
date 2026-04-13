# 재귀없는 deque

import sys
input = sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
n+=1
g=[[]for i in range(n)]

deg=[0]*n

for i in range(m):
  a,b=map(int,input().split())
  g[a]+=b,
  deg[b]+=1

q=deque()
for i in range(1,n):
  if deg[i]==0:q.append(i)

while q:
  i=q.popleft()
  print(i,end=" ")
  for j in g[i]:
    deg[j]-=1
    if deg[j]==0:q.append(j)
