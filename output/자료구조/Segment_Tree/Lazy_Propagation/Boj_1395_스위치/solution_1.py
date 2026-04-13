import sys
input = sys.stdin.readline

def app(i,v):
  st[i]=v-st[i]
  lz[i]=v-lz[i]

def push(i):
  for p in range(h,0,-1):
    j=i>>p
    if lz[j]:
      app(j<<1,lz[j]>>1)
      app(j<<1|1,lz[j]>>1)
      lz[j]=0

def pull(i):
  while i>1:
    i>>=1
    st[i]=st[i<<1]+st[i<<1|1]
    if lz[i]:st[i]=lz[i]-st[i]

def up(i,j):
  i+=s;j+=s;k=1
  a,b=i,j
  while i<=j:
    if i&1:app(i,k);i+=1
    if j&1<1:app(j,k);j-=1
    i>>=1;j>>=1;k<<=1
  pull(a);pull(b)

def qu(i,j):
  i+=s;j+=s;r=0
  push(i);push(j)

  while i<=j:
    if i&1:r+=st[i];i+=1
    if j&1<1:r+=st[j];j-=1
    i>>=1;j>>=1

  print(r)

n,m=map(int,input().split())
n+=1;s=1

while s<=n:s<<=1
h=s.bit_length()
st=[0]*(s<<1)
lz=st[:]

for i in range(m):
  a,b,c=map(int,input().split())
  if a<1:up(b,c)
  else:qu(b,c)
