from bisect import bisect_left as L

N=int(input())
A=sorted([[*map(int,input().split())]for i in range(N)])
t=[1]*N

k=A[N-1][1]
for i in range(N-2,-1,-1):
  if k>=A[i][1]:t[i]=0
  else:k=A[i][1]

a=[];b=[]
for i in range(N):
  if t[i]:
    a.append(A[i][0])
    b.append(A[i][1])

n=len(a)
dp=[0]*(n+1)

junction=[0]
index=[-1]

for i in range(n-1):
  #y=b_(i+1)*x+dp_i
  id=index[L(junction,a[i])-1]
  dp[i]=dp[id]+a[i]*b[id+1]

  x=(dp[i]-dp[i-1])/(b[i]-b[i+1])
  while x<=junction[-1]:
    junction.pop();index.pop()
    j=index[-1]
    x=(dp[i]-dp[j])/(b[j+1]-b[i+1])
  junction.append(x)
  index.append(i)

id=index[L(junction,a[n-1])-1]
dp[n-1]=dp[id]+a[n-1]*b[id+1]
print(dp[n-1])
