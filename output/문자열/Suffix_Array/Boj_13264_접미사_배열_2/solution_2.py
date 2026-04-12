#2 counting sort
#O(nlogn)

S=input()
n=len(S);m=max(n,150)+1
rank=[ord(i) for i in S]+[0]*n
if n==1:rank[0]=1   #lcp 구할때 인덱스 에러 방지
temp=[0]*(2*n)
C=[0]*m
SA=list(range(n))

k=1
while True:
  C[:m]=[0]*m
  for i in range(k,n+k):C[rank[i]]+=1
  for i in range(m-1):C[i+1]+=C[i]
  for i in range(n-1,-1,-1):
    C[rank[i+k]]-=1
    temp[C[rank[i+k]]]=i

  C[:m]=[0]*m
  for i in range(n):C[rank[i]]+=1
  for i in range(m-1):C[i+1]+=C[i]
  for i in range(n-1,-1,-1):
    x=temp[i]
    C[rank[x]]-=1
    SA[C[rank[x]]]=x

  temp[SA[0]]=1
  for i in range(1,n):
    a,b=SA[i],SA[i-1]
    temp[a]=temp[b]+((rank[a],rank[a+k])!=(rank[b],rank[b+k]))

  temp,rank=rank,temp
  if rank[SA[-1]]==n:break
  m=rank[a]+1
  k<<=1

print(*SA)
