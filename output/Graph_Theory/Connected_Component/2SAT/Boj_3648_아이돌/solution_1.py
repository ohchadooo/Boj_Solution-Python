import sys
sys.setrecursionlimit(100000)

def f(x):
  global st
  nv[x]=0
  for i in F[x]:
    if nv[i]:f(i)
  st+=x,

def bb(x):
  global S
  if T[-x]:return 0
  T[x]=1
  nv[x]=0
  S.append(x)
  for i in B[x]:
    if nv[i]:bb(i)
  return 1

while 1:
  try:
    n,m=map(int,input().split())
    k=2*n+1
    F=[[]for i in range(k)]
    B=[[]for i in range(k)]
    F[-1].append(1);B[1].append(-1)
    for i in range(m):
      a,b=map(int,input().split())
      F[-a].append(b);B[b].append(-a)
      F[-b].append(a);B[a].append(-b)
    nv=[1]*k
    st=[]
    for i in range(-n,n):
      if nv[i]:f(i)
    for i in range(-n,n):nv[i]=1
    T=[0]*k
    an=1
    while st:
      i=st.pop()
      S=[]
      if nv[i]:an=bb(i)
      while S:T[S.pop()]=0
    print(['no','yes'][an])

  except:break
