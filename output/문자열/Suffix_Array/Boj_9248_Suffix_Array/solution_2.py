# sa-k technique

S=input()
n=len(S);m=max(n,200)+1

rank=[ord(i) for i in S]+[0]*n
if n==1:rank[0]=0
nr=[0]*(2*n)
SA=[0]*n

C=[0]*m
for i in range(n):C[rank[i]]+=1
for i in range(m-1):C[i+1]+=C[i]
for i in range(n-1,-1,-1):
  C[rank[i]]-=1
  SA[C[rank[i]]]=i

k=1
while k<n:

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
    x=rank[nr[i]]
    C[x]-=1
    SA[C[x]]=nr[i]

  nr,rank=rank,nr
  sv=SA[0]
  j=1
  for i in SA:
    if nr[i]!=nr[sv] or nr[i+k]!=nr[sv+k]:
      j+=1
      sv=i
    rank[i]=j

  m=j+1
  k<<=1

S+="."
lcp=[0]*n;lcp[0]="x";j=0

for i in range(n):
  if rank[i]<2:continue
  x=SA[rank[i]-2]
  while S[i+j]==S[x+j]:j+=1
  lcp[rank[i]-1]=j
  if j:j-=1

print(*(i+1 for i in SA))
print(*lcp)
