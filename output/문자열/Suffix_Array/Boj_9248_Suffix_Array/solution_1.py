# O(nlogn) counting sort

S=input()
n=len(S);m=max(n,200)+1

rank=[ord(S[i]) for i in range(n)]+[0]*n
SA=[0]*n
rev=range(n-1,-1,-1)

k=1
C=[0]*m
temp=[0]*n
nr=[0]*(2*n)

while k<n:
  C[:m]=[0]*m
  for i in range(n):C[rank[i+k]]+=1
  for i in range(m-1):C[i+1]+=C[i]
  for i in rev:
    C[rank[i+k]]-=1
    temp[C[rank[i+k]]]=i

  C[:m]=[0]*m
  for i in range(n):C[rank[i]]+=1
  for i in range(m-1):C[i+1]+=C[i]
  for i in rev:
    x=temp[i]
    C[rank[x]]-=1
    SA[C[rank[x]]]=x

  sv=SA[0]
  j=1
  for i in SA:
    if rank[i]!=rank[sv] or rank[i+k]!=rank[sv+k]:
      j+=1
      sv=i
    nr[i]=j

  nr,rank=rank,nr
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
