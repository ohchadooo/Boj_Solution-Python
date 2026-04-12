def tree(i=1):
  nvis[i]=0
  child=[]
  for j in conn[i]:
    if nvis[j]:tree(j);child+=j,

  for c in child:
    a=b=inf;p=0
    for j in range(k):
      if dp[c][j]<=b:
        a=b;b=dp[c][j];p=j
      elif dp[c][j]<a:a=dp[c][j]

    for j in range(k):
      if j!=p:dp[i][j]+=b
      else:dp[i][j]+=a

n=int(input())
inf=10**9
a=n;k=0
while a:
  a>>=1;k+=1

dp=[[*range(1,k+1)] for i in range(n+1)]
conn=[[] for i in range(n+1)]

for i in range(n-1):
  a,b=map(int,input().split())
  conn[a]+=b,;conn[b]+=a,

nvis=[1]*(n+1)
tree()

print(min(dp[1]))
