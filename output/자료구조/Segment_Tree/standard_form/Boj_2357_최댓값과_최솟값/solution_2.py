def up(i,v):
  i+=s
  while i:
    if v<T1[i]:T1[i]=v
    if v>T2[i]:T2[i]=v
    i>>=1

def q(i,j):
  i+=s;j+=s;r=inf;e=0
  while i<=j:
    if j&1==0:
      if r>T1[j]:r=T1[j]
      if e<T2[j]:e=T2[j]
      j-=1
    if i&1:
      if r>T1[i]:r=T1[i]
      if e<T2[i]:e=T2[i]
      i+=1
    j>>=1;i>>=1
  return r,e

n,m=map(int,input().split())

inf=1e9+1
s=1
while s<n:s<<=1

T1=[inf]*(s<<1)
T2=[0]*(s<<1)

for i in range(n):
  up(i,int(input()))

for j in range(m):
  a,c=map(int,input().split())
  print(*q(a-1,c-1))
