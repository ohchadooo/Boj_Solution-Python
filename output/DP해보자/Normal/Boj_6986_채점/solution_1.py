# 150000 bitset

n=int(input())
a=[*map(int,input().split())]
k=int(input())

s=[0]
for i in range(n):
  s.append(s[-1]+a[i])

dp=[1]*(n+2)
for i in range(n+2):
  t=0
  for j in range(i+1,n+2):
    t+=s[j-1]-s[i]
    dp[j]|=dp[i]<<t

p=dp[n+1]
x=1<<k

cnt=0
if p>x:
  while p&x:
    p>>=1
    cnt+=1

print(k+cnt)
