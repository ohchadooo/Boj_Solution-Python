## 1167 트리의 지름

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(i,d,p):
  global M
  a=b=0
  for j,c in g[i]:
    if j==p:continue
    x=dfs(j,d+c,i)-d
    if x>a:b,a=a,x
    elif x>b:b=x
  M=max(M,a+b)
  return a+d

n=int(input())

g=[[]for i in range(n+1)]
for i in range(n):
  a,*b=map(int,input().split())
  for j in range(0,len(b)-1,2):
    g[a]+=(b[j],b[j+1]),

M=0
dfs(1,0,-1)
print(M)
