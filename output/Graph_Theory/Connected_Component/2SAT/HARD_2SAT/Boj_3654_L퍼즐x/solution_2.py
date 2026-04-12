def f():
  for i in range(n):
    for j in range(m):
      if a[i][j]=="W":
        for i in range(4):
          if 0<=i+di<n and 0<=j+dj<n:
            if a[i+di][j+dj]=="B":
              graph[i+di][j+dj][di].append(-dj)
              return 0
  return 1



di=[0,-1,0,1]

dj=[-1,0,1,0]
for i in range(T):
  n,m=map(int,input().split())
  a=[input().strip for i in range(n)]
  graph=[[[[for l in range(2)]for k in range(2)]for j in range(m)]for i in range(n)]


