import sys
input = sys.stdin.readline

def app(i,c):st[i]=lz[i]=c

def push(i):
  for p in range(h,0,-1):
    j=i>>p
    if lz[j]:
      app(j<<1,lz[j]);app(j<<1|1,lz[j])
      lz[j]=0

def pull(i):
  while i>1:
    i>>=1
    if lz[i]<1:st[i]=st[i<<1]|st[i<<1|1]

def up(i,j,c):
  i+=s;j+=s;a,b=i,j
  push(a);push(b)
  while i<=j:
    if i&1:app(i,1<<c);i+=1
    if j&1<1:app(j,1<<c);j-=1
    i>>=1;j>>=1
  pull(a);pull(b)

def qu(i,j):
  if i>j:i,j=j,i
  i+=s;j+=s;r=0
  push(i);push(j)
  while i<=j:
    if i&1:r|=st[i];i+=1
    if j&1<1:r|=st[j];j-=1
    i>>=1;j>>=1
  print(r.bit_count())

n,t,q=map(int,input().split())
n+=1;s=1
while s<=n:s<<=1
h=s.bit_length()

st=[2]*(s<<1)
lz=[0]*(s<<1)

for i in range(q):
  a,*b=input().split()
  b=[int(i)for i in b]
  if b[0]>b[1]:b[:2]=b[1],b[0]
  if a=="C":up(*b)
  else:qu(*b)
