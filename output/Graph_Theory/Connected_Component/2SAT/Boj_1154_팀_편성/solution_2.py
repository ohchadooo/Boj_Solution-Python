n=int(input())+1
gr=[[1]*n for i in range(n)]

while (t:=tuple(map(int,input().split())))!=(-1,-1):
  a,b=t
  if a>b:a,b=b,a
  gr[a][b]=0

F=[[]for i in range(2*n)]

for i in range(1,n-1):
  for j in range(i+1,n):
    if gr[i][j]:
      F[i].append(-j);F[j].append(-i)
      F[-i].append(j);F[-j].append(i)

T=[-1]*n
T[1]=1

def f():
  stack=[1]
  while stack:
    i=stack.pop()
    for j in F[i]:
      if j>0:
        if T[j]==0:return 1
        elif T[j]<0:
          T[j]=1
          stack.append(j)
      else:
        if T[-j]==1:return 1
        elif T[-j]<0:
          T[-j]=0
          stack.append(j)

if f():print(-1)
else:
  print(1)
  A=[];B=[]
  for i in range(1,n):
    if T[i]:A.append(i)
    else:B.append(i)
  print(*A,-1)
  print(*B,-1)
