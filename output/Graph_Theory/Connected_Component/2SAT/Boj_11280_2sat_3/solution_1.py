def fordfs(i):
  vis[i]=0
  for j in forw[i]:
    if vis[j]:fordfs(j)
  stack.append(i)

def backdfs(i):
  vis[i]=0
  if check[-i]:global T; T=0; return
  check[i]=1
  SCC.append(i)
  for j in back[i]:
    if vis[j]:backdfs(j)

n,m=map(int,input().split())
v=2*n+1

forw=[[]for i in range(v+1)]
back=[[]for i in range(v+1)]

for i in range(m):
  a,b=map(int,input().split())
  forw[-a].append(b);forw[-b].append(a)
  back[b].append(-a);back[a].append(-b)

vis=[1]*v
stack=[]

#forward dfs
for i in range(-n,0):
  if vis[i]:fordfs(i)
for i in range(1,n+1):
  if vis[i]:fordfs(i)

#backward dfs
T=1
check=[0]*v
SCC=[]

for i in range(1,v):vis[i]=1
while stack:
  i=stack.pop()
  if vis[i]:
    while SCC:check[SCC.pop()]=0
    backdfs(i)

print(T)
