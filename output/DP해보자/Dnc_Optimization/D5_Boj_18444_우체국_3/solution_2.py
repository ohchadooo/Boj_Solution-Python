# 우체국 2
v,p,l=map(int,input().split())
A=[*map(int,input().split())]

T=0
if p==1:
  T=1;p+=1

inf=10**18
dp=[[[[inf,0]]*v for j in range(v)]for i in range(p-1)]

for i in range(v):
  for j in range(v):
    dp[0][i][j]=[0,j]
    if i<j:
      for k in range(i+1,j):
        dp[0][i][j][0]+=min(A[k]-A[i],A[j]-A[k])
    else:
      for k in range(i+1,v):
        dp[0][i][j][0]+=min(A[k]-A[i],l+A[j]-A[k])
      for k in range(j):
        dp[0][i][j][0]+=min(A[j]-A[k],l+A[k]-A[i])

for t in range(1,p-1):
  for i in range(v-2):
    for j in range(i+2,v):
      dp[t][i][j]=min((dp[t-1][i][w][0]+dp[0][w][j][0],w) for w in range(i+1,j))

if T:
  a=min(dp[0][i][i] for i in range(v))
  print(a[0])
  print(A[a[1]])

else:
  ans=inf
  for i in range(v-1):
    for j in range(i+1,v):
      x=dp[p-2][i][j][0]+dp[0][j][i][0]
      if x<ans:
        st=i
        tr=[j]
        ans=x

  print(ans)

  k=p-2
  while k:
    tr.append(dp[k][st][tr[-1]][1])
    k-=1

  print(A[st],end=" ")
  print(*[A[i] for i in tr[::-1]])
