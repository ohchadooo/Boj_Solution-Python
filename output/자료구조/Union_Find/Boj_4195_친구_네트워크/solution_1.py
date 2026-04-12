#집합크기 보존

def union(x,y):
  a,b=find(x),find(y)
  if a==b:return p[a]
  if p[a]>p[b]:b,a=a,b
  p[a]+=p[b]
  p[b]=a
  return p[a]

def find(x):
  if p[x]<0:return x
  p[x]=find(p[x])
  return p[x]

t=int(input())

for i in range(t):
  f=int(input())
  p=[-1]*(2*f)

  fr={}
  x=-1
  for j in range(f):
    a,b=input().split()
    for h in [a,b]:
      if h not in fr:fr[h]=(x:=x+1)
    print(-union(fr[a],fr[b]))
