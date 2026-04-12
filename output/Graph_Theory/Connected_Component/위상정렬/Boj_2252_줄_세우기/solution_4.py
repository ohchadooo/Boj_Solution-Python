#사이클 판별!!
#Boj 2623 음악프로그램

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(i):
  if ch[i]==1:return 1
  if ch[i]:return
  ch[i]=1
  for j in g[i]:
    if dfs(j):return 1
  ch[i]=2
  ans.append(i)

n,m=map(int,input().split())
n+=1

g=[[]for i in range(n)]
for i in range(m):
  l,*a=map(int,input().split())
  for j in range(l-1):
    g[a[j+1]]+=a[j],

ch=[0]*n
ans=[]
for i in range(1,n):
  if ch[i]<1:
    if dfs(i):ans=[0];break

print(*ans)
