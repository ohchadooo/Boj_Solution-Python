import sys
input = sys.stdin.readline

def app(i,v,k):
  lz1[i]+=v;lz2[i]+=k

def push(i):
  i+=s
  for p in range(h,0,-1):
    j=i>>p
    if lz1[j]:
      app(j<<1,lz1[j],lz2[j])
      app(j<<1|1,lz1[j]+lz2[j]*fl[j<<1],lz2[j])
      lz1[j]=lz2[j]=0
  print(S[i-s]+lz1[i])

def up(i,j):
  i+=s;j+=s
  p,q=1,j-i+2
  while i<=j:
    if i&1:app(i,p,1);p+=fl[i];i+=1
    if j&1<1:q-=fl[j];app(j,q,1);j-=1
    i>>=1;j>>=1

n=int(input())+1
s=1
while s<=n:s<<=1
h=s.bit_length()

lz1=[0]*(s<<1)
lz2=lz1[:]
fl=lz1[:]

for i in range(h):
  x=s>>i
  for j in range(x,x<<1):fl[j]=1<<i

S=[0]+[*map(int,input().split())]

for i in range(int(input())):
  a,*b=map(int,input().split())
  if a<2:up(*b)
  else:push(*b)
