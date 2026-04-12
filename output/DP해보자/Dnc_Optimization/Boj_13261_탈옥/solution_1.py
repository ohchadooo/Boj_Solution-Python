def dnc(s,e,p,q):
  m=(s+e)>>1

  opt=p
  mini=inf
  for i in range(p,min(m+1,q)):
    k=dp[i][x-1]+(m-i)*(S[m]-S[i])
    if k<mini:
      opt=i
      mini=k

  dp[m][x]=mini

  if s+2>e:return

  dnc(s,m,p,opt+1)
  dnc(m,e,opt,q)

l,g=map(int,input().split())
l+=1
C=[0]+[*map(int,input().split())]

inf=10**18

S=[0]
for i in range(1,l):
  S+=S[-1]+C[i],

dp=[[0]*g for i in range(l)]  #dp[g][i] g:count, i:0~i
for i in range(l):
  dp[i][0]=S[i]*i

for x in range(1,g):
  dnc(1,l,1,l)

print(dp[l-1][g-1])
