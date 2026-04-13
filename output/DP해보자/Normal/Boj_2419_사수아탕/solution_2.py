n,m=map(int,input().split())
pos=[0];neg=[0]

ans=0
for i in range(n):
  x=int(input())
  if x>0:pos.append(x)
  elif x==0:ans+=m
  else:neg.append(-x)

pos.sort();neg.sort()
x,y=len(neg),len(pos)
dp=[[[0]*(x+y-1) for i in range(y)] for i in range(x)]  #left w,d right w,d

for bas in range(x+y-1):
  dp[0][0][bas]=m*bas,m*bas

  for i in range(1,min(x,bas+1)):
    w=dp[i-1][0][bas][0]-(neg[i]-neg[i-1])*(bas-i+1)
    dp[i][0][bas]=w,w-neg[i]*(bas-i)
    if i>bas:break

  for j in range(1,min(y,bas+1)):
    w=dp[0][j-1][bas][1]-(pos[j]-pos[j-1])*(bas-j+1)
    dp[0][j][bas]=w-pos[j]*(bas-j),w

  for i in range(1,min(x,bas)):
    for j in range(1,min(y,bas-i+1)):
      a,b=dp[i-1][j][bas]
      a-=(neg[i]-neg[i-1])*(bas-i-j+1)
      b-=(pos[j]+neg[i])*(bas-i-j+1)
      a=max(a,b)

      c,d=dp[i][j-1][bas]
      d-=(pos[j]-pos[j-1])*(bas-i-j+1)
      c-=(pos[j]+neg[i])*(bas-i-j+1)
      c=max(c,d)

      dp[i][j][bas]=a,c

Max=max([max(dp[i][j][i+j])for i in range(x) for j in range(y)])
print(ans+Max)
