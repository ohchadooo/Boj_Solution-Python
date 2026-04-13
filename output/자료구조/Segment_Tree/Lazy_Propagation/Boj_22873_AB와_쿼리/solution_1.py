import sys
input = sys.stdin.readline

def app(i,v):
  if v==9:st[i]=2
  elif v==0:st[i]=1
  else:st[i]=0
  C[i-s]=v;lz[i]=0
  pull(i)

def push(i):
  for p in range(h,0,-1):
    j=i>>p
    if lz[j]:
      st[j<<1]=lz[j<<1]=st[j<<1|1]=lz[j<<1|1]=lz[j]
      lz[j]=0

  if lz[i]==2:C[i-s]=9;lz[i]=0
  elif lz[i]==1:C[i-s]=0;lz[i]=0

def pull(i):
  while i>1:
    i>>=1
    st[i]=lz[i] if lz[i] else st[i<<1|1]&st[i<<1]

def qu(S):
  a,i,d=S.split()
  i=int(i)-1;d=int(d)
  if a=="A":print(up(i,d-A[i]));A[i]=d
  else:print(up(i,d-B[i]));B[i]=d

def up(i,v):
  if v==0:return 0
  push(i+s)
  k=C[i]+v
  i+=s
  if 0<=k<10:
    app(i,k)
    return 1
  if k<0:k+=10;ty=1
  else:k-=10;ty=2

  app(i,k)

  ff=find(i+1,ty)

  if ff>i+1:
    push(ff-1);push(ff)
    rup(i+1,ff-1,3-ty)
  app(ff,C[ff-s]+2*ty-3)

  return ff-i+1

def rup(i,j,ty):
  a,b=i,j
  while i<=j:
    if i&1:st[i]=lz[i]=ty;i+=1
    if j&1<1:st[j]=lz[j]=ty;j-=1
    i>>=1;j>>=1
  pull(a);pull(b)

def find(i,ty):
  push(i);push(s+n-1)
  while i>1:
    if i&1:
      if st[i]!=ty:break
      i+=1
    i>>=1
  while i<s:
    if lz[i]:
      st[i<<1]=lz[i<<1]=st[i<<1|1]=lz[i<<1|1]=lz[i]
      lz[i]=0
    if st[i<<1]!=ty:i<<=1
    else:i=i<<1|1
  return i

n,q=map(int,input().split())

A=[int(i) for i in input().strip()]
B=[int(i) for i in input().strip()]
A.reverse()
B.reverse()
n+=1

s=1
while s<n:s<<=1
st=[1]*(s<<1)  # 1:전부 0. 2:전부 9. 0:둘다 아님.
lz=[0]*(s<<1)
h=s.bit_length()-1
C=[0]*n

t=0
for i in range(n-1):
  t,x=divmod(t+A[i]+B[i],10)
  up(i,x)
up(n-1,t)

for i in range(q):qu(input().strip())
