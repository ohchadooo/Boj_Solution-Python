#rabin-karp

n=int(input())-1
a=list(map(ord,input()))

base=131
mod=10**9+7

x=y=M=0
k=1
for i in range(n):
  x=(x*base+a[i])%mod
  y=(y+k*a[n-i])%mod
  k=k*base%mod

  if x==y:M=i+1

print(n-M+1)
