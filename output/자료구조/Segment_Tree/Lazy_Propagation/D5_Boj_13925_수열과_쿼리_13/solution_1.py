import sys
input = sys.stdin.readline

def app(i,x,v):
  L=lz[x]
  if i==1:
    L[0]=(L[0]+v)%E
    st[x]=(st[x]+v*fl[x])%E
  elif i==2:
    L[1]=L[1]*v%E
    st[x]=st[x]*v%E
    L[0]=L[0]*v%E
  else:
    L[2]=v
    st[x]=fl[x]*v%E
    L[0]=0;L[1]=1

def push(i):
  for p in range(h,0,-1):
    j=i>>p
    L=lz[j]
    for k in [2,1,0]:
      if L[k] or (k==1 and L[k]>1):
        app(k+1,j<<1,L[k]);app(k+1,j<<1|1,L[k])
        L[k]=0 if k!=1 else 1

def pull(i):
  while i>1:
    i>>=1
    L=lz[i]
    if L[2]:st[i]=L[2]*fl[i]%E
    else:st[i]=(st[i<<1]+st[i<<1|1])%E
    if L[1]:st[i]=st[i]*L[1]%E
    if L[0]:st[i]=(st[i]+L[0]*fl[i])%E

def up(i,x,y,v):
  x+=s;y+=s;a,b=x,y
  push(a);push(b)
  while x<=y:
    if x&1:app(i,x,v);x+=1
    if y&1<1:app(i,y,v);y-=1
    x>>=1;y>>=1
  pull(a);pull(b)

def qu(i,j):
  i+=s;j+=s;r=0
  push(i);push(j)
  while i<=j:
    if i&1:r+=st[i];i+=1
    if j&1<1:r+=st[j];j-=1
    i>>=1;j>>=1
  print(r%E)

E=10**9+7

n=int(input())+1;s=1
while s<=n:s<<=1
h=s.bit_length()

st=[0]*(s<<1)
lz=[[0,1,0] for i in range(s<<1)]
fl=st[:]

for i in range(h):
  x=s>>i
  for j in range(x,x<<1):fl[j]=1<<i

st[s+1:s+n]=[*map(int,input().split())]
for i in range(s-1,0,-1):st[i]=(st[i<<1]+st[i<<1|1])%E

for _ in range(int(input())):
  a,*b=map(int,input().split())
  if a<4:up(a,*b)
  else:qu(*b)
