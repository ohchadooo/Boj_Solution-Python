#우체국 1

v,p,l=map(int,input().split())
A=[*map(int,input().split())]

inf=10**18
minar=[inf]*v

x=1<<v
ans=inf
pos=0

for i in range(x):
  if i.bit_count()==p:
    for j in range(v):
      if i&(1<<j):
        for k in range(v):
          t=abs(A[j]-A[k])
          minar[k]=min(minar[k],t,l-t)

  S=sum(minar)
  if S<ans:
    ans=S
    pos=i
  for i in range(v):minar[i]=inf

print(ans)
j=0
while pos:
  if pos&1:print(A[j],end=" ")
  pos>>=1
  j+=1
