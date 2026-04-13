from bisect import bisect_left as L

def merge(a,b):
  j=0;n=len(b);t=[]
  for i in a:
    while j<n:
      if i<=b[j]:break
      t.append(b[j]);j+=1
    t.append(i)
  return t+b[j:]

def initt():
  x,y=s>>1,s
  while x:
    for i in range(x,y):
      st[i]=merge(st[2*i],st[2*i+1])
    x>>=1;y>>=1

def q(i,j,k):
  i+=s;j+=s;r=0
  while i<=j:
    if i&1:
      r+=L(st[i],k)
      i+=1
    if j&1<1:
      r+=L(st[j],k)
      j-=1
    i>>=1;j>>=1
  return r

n=int(input())
s=1
while s<n:s<<=1
st=[[]for i in range(s<<1)]

a=[*map(int,input().split())]
for i in range(n):
  st[s+i]=[-a[i]]

initt()
print(st)

r=0
m=int(input())
for i in range(m):
  a,a,c=map(int,input().split())
  r=q((a^r)-1,(a^r)-1,-(c^r))
  print(r)
