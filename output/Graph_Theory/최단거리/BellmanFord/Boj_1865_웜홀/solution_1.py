import sys
input = sys.stdin.readline

def bel():
  n,m,w=map(int,input().split())
  g=[]
  for i in range(m):
    a,b,c=map(int,input().split())
    g.append((a,b,c));g.append((b,a,c))

  for i in range(w):
    a,b,c=map(int,input().split())
    g.append((a,b,-c))

  cost=[0]*(n+1)

  T=0
  for i in range(n):
    nup=1
    for a,b,c in g:
      if cost[b]>cost[a]+c:
        nup=0
        cost[b]=cost[a]+c
        if i==n-1:T=1;return "YES"
    if nup:break

  return "NO"

for i in range(int(input())):print(bel())
