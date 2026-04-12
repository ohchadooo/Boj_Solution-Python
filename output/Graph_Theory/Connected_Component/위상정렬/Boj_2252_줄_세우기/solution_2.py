# dfs method 1 (like Kosaraju)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

def dfs(i):
  t=0
  for j in g[i]:
    if deg[j]:dfs(j)
  deg[i]=0
  ans.append(i)

n,m=map(int,input().split())
n+=1
g=[[]for i in range(n)]

deg=[1]*n

for i in range(m):
  a,b=map(int,input().split())
  g[a]+=b,

ans=[]
for i in range(1,n):
  if deg[i]:dfs(i)

ans.reverse()
print(*ans)
