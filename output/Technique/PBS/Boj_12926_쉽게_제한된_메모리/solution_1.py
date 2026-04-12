from bisect import bisect_right as R

n,x,a,b=map(int,input().split())

q=int(input())
mod=10**9+7

Q=sorted(map(int,input().split()))
l=[0]*q
h=[mod]*q
m=[mod>>1]*q
cnt=[0]*(q+1)

check=(1<<q)-1

ans=0
while check:
  y=x

  for i in range(q):
    cnt[i]=0

  for i in range(n):
    ind=R(m,y)
    cnt[ind]+=1

    y=(y*a+b)%mod

  for i in range(q):
    cnt[i+1]+=cnt[i]

    if l[i]+1==h[i]:
      ans+=l[i]
      check=~((~check)|(1<<i))
      continue

    if Q[i]<cnt[i]:h[i]=m[i]
    else:l[i]=m[i]
    m[i]=(l[i]+h[i])>>1

print(ans)
