n=int(input())
A=[*map(int,input().split())]
k=int(input())
i=j=s=c=0
while j<n:
  if s<=k:s+=A[j];j+=1
  while s>k:
    c+=n-j+1
    s-=A[i]
    i+=1
print(c)
