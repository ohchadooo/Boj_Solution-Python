n=int(input())
a=[0]+[*map(int,input().split())]

inf=10**9
dp=[[inf]*(n+1) for i in range(n+1)]

dp[1][0]=0

for i in range(1,n):
  a[0]=a[i+1]
  for j in range(i):
    dp[i+1][j]=min(dp[i+1][j],dp[i][j]+abs(a[i+1]-a[i]))
    dp[i+1][i]=min(dp[i+1][i],dp[i][j]+abs(a[i+1]-a[j]))

print(min(dp[-1]))
