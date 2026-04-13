#속도 개선

def union(a,b):
  x=find(a)
  y=find(b)
  if x!=y:p[y]=x

def find(a):
  while a!=p[a]:
    a=p[a]
  return a

n,m=map(int,input().split())

p=[*range(n+1)]
S=[]

for i in range(m):
  t,a,b=map(int,input().split())
  if t:print("yes" if find(a)==find(b) else "no")
  else:union(a,b)
