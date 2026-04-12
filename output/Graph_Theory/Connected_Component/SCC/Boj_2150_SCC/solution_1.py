# Kosaraju's Algorithm

def fordfs(i):
  vis[i]=0
  for j in forw[i]:
    if vis[j]:fordfs(j)
  stack.append(i)

def backdfs(i):
  vis[i]=0
  SCC[-1].append(i)
  for j in back[i]:
    if vis[j]:backdfs(j)

v,e=map(int,input().split())

forw=[[]for i in range(v+1)]
back=[[]for i in range(v+1)]

for i in range(e):
  a,b=map(int,input().split())
  forw[a].append(b)
  back[b].append(a)

vis=[1]*(v+1)
stack=[]

SCC=[]

#forward dfs
for i in range(1,v+1):
  if vis[i]:fordfs(i)

print(stack)

#backward dfs
for i in range(1,v+1):vis[i]=1
while stack:
  i=stack.pop()
  if vis[i]:
    SCC.append([])
    backdfs(i)

n=len(SCC)
print(n)
for i in range(n):
  SCC[i].sort()

SCC.sort()
for i in range(n):
  print(*SCC[i],-1)
