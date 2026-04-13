n=int(input())
A=[*map(int,input().split())]

c=10**10
i=0;j=n-1
while i<j:
  x=A[i]+A[j]
  if abs(x)<c:
    c=abs(x);opt=A[i],A[j]
  if x>0:j-=1
  else:i+=1

print(*opt)
