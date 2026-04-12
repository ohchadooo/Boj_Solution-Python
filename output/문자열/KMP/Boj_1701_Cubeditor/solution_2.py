##Suffix Array

S="abcabcabc"
n=len(S)

rank=[ord(S[i]) for i in range(n)]+[-1]*n

def R(k):
  global rank
  temp=[0]*n

  arr=list(range(n))
  arr.sort(key=lambda i:(rank[i],rank[i+k]))

  sv=arr[0]
  for i in arr:
    if (rank[i],rank[i+k])!=(rank[sv],rank[sv+k]):
      temp[i]=temp[sv]+1
      sv=i
    else:
      temp[i]=temp[sv]
    sv=i

  for i in range(n):rank[i]=temp[i]

k=1
while k<n:
  R(k)
  k<<=1

SA=[0]*n
for i in range(n):SA[rank[i]]=i

M=j=0
for i in range(n):
  if rank[i]<1:continue
  x=SA[rank[i]-1]
  while i+j<n and x+j<n and S[i+j]==S[x+j]:
    j+=1
  if M<j:M=j
  if j:j-=1

print(M)
