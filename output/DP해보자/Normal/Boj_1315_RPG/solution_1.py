n=int(input())

a=[(0,0,0)]+sorted(tuple(map(int,input().split())) for i in range(n))  #str sort
n+=1
b=sorted((a[i][1],i,a[i][2])for i in range(n))  #int sort

dp=[[0]*(n+1) for i in range(n+1)]  #dp[i][j]  i-str quest, j-int quest
dp[0][0]=[2,0]

M=0

for i in range(n-1):
  x,y=dp[i][0]
  if x-1<a[i+1][0]:dp[i+1][0]=[-1,0]
  else:
    dp[i+1][0]=[x+a[i+1][2],y+1]
    M=y+1
for j in range(n-1):
  x,y=dp[0][j]
  if x-1<b[j+1][0]:dp[0][j+1]=[-1,0]
  else:
    dp[0][j+1]=[x+b[j+1][2],y+1]
    M=max(M,y+1)

for i in range(1,n):
  vis=[1]*n
  for j in range(1,n):
    vis[b[j][1]]=0
    if dp[i][j-1][0]>=a[i][0]+b[j][0]:
      x,y=dp[i][j-1]
      if i<b[j][1]:
        x+=b[j][2]
        y+=1
      dp[i][j]=[x,y]
      M=max(M,y)

    elif dp[i-1][j][0]>=a[i][0]+b[j][0]:
      x,y=dp[i-1][j]
      if vis[i]:
        x+=a[i][2]
        y+=1
      dp[i][j]=[x,y]
      M=max(M,y)
    else:dp[i][j]=[-1,0]

print(M)
