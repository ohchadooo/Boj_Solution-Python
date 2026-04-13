def up(i,a):
  i+=s-1
  while i>=0:
    st[i]+=a
    i=(i-1)>>1

def find(x):
  i=0
  while i<s-1:
    if x>=st[2*i+2]:
      x-=st[2*i+2]
      i=2*i+1
    else:i=2*i+2
  return i-s+1

n=int(input())
L=[*map(int,input().split())]

s=1
while s<n:s<<=1
st=[0]*(s<<1)

for i in range(n):
  up(i,1)

ans=[0]*n
for i in range(n-1,-1,-1):
  id=find(L[i])
  ans[id]=i+1
  up(id,-1)

print(*ans)
