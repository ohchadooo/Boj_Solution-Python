#sa-k technique

S=input()
n=len(S);m=max(n,150)+1
rank=[ord(i) for i in S]+[0]*n
if n==1:rank[0]=1   #lcp 구할때 인덱스 에러 방지
nr=[0]*(2*n)
C=[0]*m
SA=list(range(n))

for i in range(n):C[rank[i]]+=1
for i in range(m-1):C[i+1]+=C[i]
for i in range(n-1,-1,-1):
  C[rank[i]]-=1
  SA[C[rank[i]]]=i

k=1
while True:
  for i in range(k):nr[i]=i+n-k
  p=k
  for i in range(n):
    if SA[i]>=k:
      nr[p]=SA[i]-k
      p+=1

  C[:m]=[0]*m
  for i in range(n):C[rank[i]]+=1
  for i in range(m-1):C[i+1]+=C[i]
  for i in range(n-1,-1,-1):
    C[rank[nr[i]]]-=1
    SA[C[rank[nr[i]]]]=nr[i]

  nr[SA[0]]=1
  for i in range(1,n):
    a,b=SA[i],SA[i-1]
    nr[a]=nr[b]+((rank[a],rank[a+k])!=(rank[b],rank[b+k]))

  nr,rank=rank,nr
  if rank[SA[-1]]==n:break
  m=rank[a]+1
  k<<=1

print(*SA)
