n=int(input())
a=[*map(int,input().split())]
s=sum(a)+1

dp=[-1]*s
dp[0]=0

temp=dp[:]

for i in range(n):
  for j in range(s-1,-1,-1):
    if dp[j]>=0:
      temp[j+a[i]]=max(temp[j+a[i]],dp[j]+a[i])
      if j>a[i]:
        temp[j-a[i]]=max(temp[j-a[i]],dp[j])
      else:
        temp[a[i]-j]=max(temp[a[i]-j],dp[j]-j+a[i])
  dp=temp[:]

print(dp[0] if dp[0] else -1)
