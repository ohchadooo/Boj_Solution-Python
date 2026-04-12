import sys
input = sys.stdin.readline

def bel():
  n,k=map(int,input().split())

  g=[]
  dd=[0]*(n+1)

  for i in range(k):
    a,b,c,d=map(int,input().split())
    if a!=2:g.append((b,c,d))
    if a!=1:g.append((c,b,-d))

  for i in range(n):
    for b,c,d in g:
      if dd[c]<dd[b]+d:
        dd[c]=dd[b]+d
        if i==n-1:return -1

  x=max(dd)
  if x<101:return x
  return -1

print(bel())
