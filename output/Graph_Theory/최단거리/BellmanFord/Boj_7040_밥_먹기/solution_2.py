input_data = """\
5 2 2
1 5 10
2 4 5
2 3 3
3 4 3
"""

import sys
from io import StringIO

sys.stdin = StringIO(input_data)

import sys
input = sys.stdin.readline

def bel():
  n,x,y=map(int,input().split())
  g=[]
  for i in range(x):
    a,b,d=map(int,input().split())
    g.append((a,b,d))
  for i in range(y):
    a,b,d=map(int,input().split())
    g.append((b,a,-d))

  inf=10**18
  dis=[inf]*(n+1);dis[1]=0

  for i in range(n):
    for a,b,d in g:
      if dis[a]!=inf and dis[b]>dis[a]+d:
        dis[b]=dis[a]+d

  if dis[n]==inf:return -2
  return dis[n]


print(bel())
