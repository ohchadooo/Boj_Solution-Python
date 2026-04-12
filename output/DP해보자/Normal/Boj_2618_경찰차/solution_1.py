def f(a,b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])

def g(v,r):
  x,y=dp[v][r]
  x+=f(a[v+1],a[v])
  if x<dp[v+1][r][0]:
    dp[v+1][r]=x,3-y


n=int(input())
w=int(input())

a=[(1,1)]
a+=[tuple(map(int,input().split())) for i in range(w)]
a+=[(n,n)]

inf=10**9
dp=[[(inf,1)]*(w+1) for i in range(w+1)] # val,position
dp[0][-1]=0,1

for i in range(w):
  for j in range(-1,i):
    x,y=dp[i][j]
    z=x+f(a[i+1],a[i])
    if z<dp[i+1][j][0]:
      dp[i+1][j]=z,y
    z=x+f(a[i+1],a[j])
    if z<dp[i+1][i][0]:
      dp[i+1][i]=z,3-y

ans=min(dp[-1])
print(ans[0])

j=dp[-1].index(ans)
if j==w:j=-1

num=[0]*w
num[w-1]=dp[-1][j][1]

for i in range(w-1,0,-1):
  if i>j:
    num[i-1]=num[i]
  else:
    num[i-1]=3-num[i]
    j-=1
    while (dp[i+1][i][0]!=dp[i][j][0]+f(a[i+1],a[j]) or dp[i+1][i][1]==dp[i][j][1]):
      j-=1

print(*num)
