def up(i,v):
  i+=s
  while i:
    t[i]+=v
    i>>=1

def f(m):
  i=1
  while i<s:
    if t[i<<1]>=m:i<<=1
    else:m-=t[i<<1];i=i*2+1
  return i-s

n,k=map(int,input().split())
A=[int(input())for i in range(n)]

m=(k+1)>>1

N=65537
s=1
while s<=N:s<<=1
t=[0]*(s<<1)

for i in range(k-1):up(A[i],1)

an=0
for i in range(n-k+1):
  up(A[i+k-1],1)
  an+=f(m)
  print(f(m))
  up(A[i],-1)

print(an)
