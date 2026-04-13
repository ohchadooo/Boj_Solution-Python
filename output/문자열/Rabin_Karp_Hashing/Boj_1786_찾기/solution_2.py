base=131
mod=10**9+7

a=[*map(ord,input())]
b=[*map(ord,input())]

m=len(b)
h=0
for j in range(m):
  h=(h*base+b[j])%mod

t=0
if len(a)>=m:
  for j in range(m):
    t=(t*base+a[j])%mod

ans=[]
if h==t:ans.append(1)

k=pow(base,m-1,mod)

for j in range(len(a)-m):
  t=((t-k*a[j])*base+a[j+m])%mod
  if h==t:ans.append(j+2)

print(len(ans))
if ans:print(*ans)
