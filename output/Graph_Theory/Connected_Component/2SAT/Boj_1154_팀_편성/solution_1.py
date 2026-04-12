n=int(input())+1
graph=[[1]*n for i in range(n)]

while (t:=tuple(map(int,input().split())))!=(-1,-1):
  a,b=t
  graph[a][b]=graph[b][a]=0

t=[0]*n

def f(x):
  stack=[x]
  t[x]=1
  while stack:
    c=stack.pop()
    for i in range(1,n):
      if i==c:continue
      if graph[c][i]:
        if t[c]==t[i]:return 1
        elif t[i]==0:
          t[i]=3-t[c]
          stack.append(i)

  for i in range(2,n):
    if t[i]==0:return f(i)

if f(1):print(-1)
else:
  A=[];B=[]
  for i in range(1,n):
    if t[i]<2:A.append(i)
    else:B.append(i)
  print(1)
  print(*A,-1)
  print(*B,-1)
