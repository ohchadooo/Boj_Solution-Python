n,m,k=map(int,input().split())

a=[[*map(int,input().split())]for _ in range(n)]

L=1<<m
inf=-20000

dp=[[0]+[inf]*k for _ in range(L)]
temp=[[0]+[inf]*k for _ in range(L)]
sum=[0]*L
TF=[0]*L

for i in range(L):
  j=3
  s=i
  while s:
    if s&j==j:TF[i]=1
    s>>=1

for i in range(n):
  for j in range(L):sum[j]=0
  for j in range(m):
    t=1<<j
    for l in range(L):
      if t&l:sum[l]+=a[i][j]
  print(sum)
  for j in range(L):
    if TF[j]:continue
    for l in range(L):
      if TF[l]:continue
      if j&l: continue
      bc=l.bit_count()
      for r in range(k-bc+1):
        if dp[j][r]==inf:continue
        temp[l][r+bc]=max(temp[l][r+bc],dp[j][r]+sum[l])
  print(temp)

  for i in range(L):
    dp[i]=temp[i][:]
    temp[i]=[0]+[inf]*k

print(max(dp[i][-1]for i in range(L)))
