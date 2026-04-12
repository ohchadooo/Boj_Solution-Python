import sys
input = sys.stdin.readline
sys.setrecursionlimit(100100)

def f(x,p):
  global M1,M2
  A=inf;B=0
  for y,c in g[x]:
    if y==p:continue

    i,j=f(y,x)
    i+=c;j+=c

    M1,M2=sorted([M1,M2,A+j,B+i,B+j])[3:]
    A,B=sorted([A,B,i,j])[2:]

  return A,B

n=int(input())+1
inf=-10**18
g=[[]for i in range(n)]

for i in range(n-2):
  a,b,c=map(int,input().split())
  g[a]+=(b,c),;g[b]+=(a,c),

M1=M2=0
f(1,0)
print(M1)
