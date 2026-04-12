from bisect import bisect as B

n=int(input())
a,b,c=map(int,input().split())

A=[*map(int,input().split())]
k=0

s=[(k:=k+i) for i in A]+[0]
q=[0]*(n+1)  # inc. slope

junction=[0]
index=[-1]

for i in range(n-1):
  # y=-2a*s[j]s[i]+q[j]
  id=index[B(junction,s[i])-1]
  q[i]=q[id]-2*a*s[id]*s[i]+2*a*s[i]**2+c

  x=(q[i]-q[i-1])/(2*a*(s[i]-s[i-1]))
  while x<=junction[-1]:
    index.pop();junction.pop()
    j=index[-1]
    x=(q[i]-q[j])/(2*a*(s[i]-s[j]))

  junction.append(x)
  index.append(i)


id=index[B(junction,s[n-1])-1]
print(q[id]-2*a*s[id]*s[n-1]+a*s[n-1]**2+b*s[n-1]+c)
