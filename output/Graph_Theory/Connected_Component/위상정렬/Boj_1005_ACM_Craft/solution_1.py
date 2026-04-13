import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x):
  t=0
  for i in graph[x]:
    if build[i]<0:dfs(i)
    t=max(t,build[i])

  build[x]=t+time[x]

for i in range(int(input())):
  n,k=map(int,input().split())
  time=[0]+[*map(int,input().split())]

  graph=[[]for i in range(n+1)]
  build=[-1]*(n+1)

  for i in range(k):
    a,b=map(int,input().split())
    graph[b]+=a,

  w=int(input())
  dfs(w)
  print(build[w])
