def up(i,v):
  a=v+d*i;b=v-u*i
  i+=s
  while i:
    if B[i]<a:B[i]=a
    if F[i]<b:F[i]=b
    i>>=1

def q(i):
  a=b=i+s
  x=inf;y=inf

  n=len(B)
  if i==n-1:x=B[1]
  while a:
    if not a&1:
      x=max(x,B[a])
      a-=1
    a>>=1
  if i==0:y=F[1]
  while b>1:
    if b&1:
      y=max(y,F[b])
      b+=1
    b>>=1
  return max(x-d*i,y+u*i)

def f(x):
  global M
  a=len(x)
  opt=[inf]*a

  st=inf
  for i in range(a):
    st=max(st-d*(x[i][1]-x[i-1][1]),q(x[i][1]))+x[i][2]
    opt[i]=max(opt[i],st)

  st=q(x[a-1][1])+x[a-1][2]
  for i in range(a-2,-1,-1):
    st=max(st-u*(x[i+1][1]-x[i][1]),q(x[i][1]))+x[i][2]
    opt[i]=max(opt[i],st)

  for i in range(a):up(x[i][1],opt[i])

n,u,d,k=map(int,input().split())
market=sorted([tuple(map(int,input().split()))for i in range(n)])

N=500001;inf=-10**18
s=1
while s<=N:
  s<<=1

B=[inf]*(s<<1)
F=[inf]*(s<<1)

up(k,0)

i=0
while i<n:
  cand=[market[i]]

  t=market[i][0]
  i+=1
  while i<n:
    if market[i][0]!=t:break
    cand.append(market[i])
    i+=1
    if i==n:break
  f(cand)

print(q(k))
