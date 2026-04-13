#Standard Form
#O(nlog^2n)

S=input()
n=len(S)
rank=[ord(i) for i in S]+[-1]*n
nr=[-1]*(2*n)
SA=[*range(n)]
k=1
while True:
  SA.sort(key=lambda x:(rank[x],rank[x+k]))
  nr[SA[0]]=0
  j=0
  for i in range(1,n):
    a,b=SA[i],SA[i-1]
    nr[a]=nr[b]+((rank[a],rank[a+k])!=(rank[b],rank[b+k]))
  nr,rank=rank,nr
  if rank[SA[-1]]==n-1:break
  k<<=1
print(*SA)
