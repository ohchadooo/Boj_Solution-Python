a=[*map(ord,input())]
b=[*map(ord,input())]

m=len(b)
h=[]
for i in (0,1):
  x=0
  for j in range(m):
    x=(x*base[i]+b[j])%mod[i]
  h.append(x)

t=[]
if len(a)>=m:
  for i in (0,1):
    x=0
    for j in range(m):
      x=(x*base[i]+a[j])%mod[i]
    t.append(x)

ans=[]
if h==t:ans.append(1)

k=[pow(base[i],m-1,mod[i]) for i in (0,1)]

for j in range(len(a)-m):
  print(h,t)
  for i in (0,1):
    t[i]=((t[i]-k[i]*a[j])*base[i]+a[j+m])%mod[i]
  if h==t:ans.append(j+2)

print(len(ans))
if ans:print(*ans)
