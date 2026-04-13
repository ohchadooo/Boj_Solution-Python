import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(i,d):
  global M
  a=b=0
  for j,c in g[i]:
    x=dfs(j,d+c)-d
    if x>a:b,a=a,x
    elif x>b:b=x
  M=max(M,a+b)
  return a+d

n=int(input())

g=[[]for i in range(n+1)]
for i in range(n-1):
  a,b,c=map(int,input().split())
  g[a]+=(b,c),

M=0
dfs(1,0)
print(M)
