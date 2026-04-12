# O(nlog^2n)
def sol():
  S=input()
  n=len(S)
  rank=[ord(i) for i in S]+[-1]*n
  nr=[-1]*(2*n)
  SA=list(range(n))
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
  Lcp(rank,SA,S)

def Lcp(rank,SA,S):
  n=len(S)
  lcp=[0]*n;lcp[0]="x"
  S+='.'
  j=0
  for i in range(n):
    ri=rank[i]
    if ri<1:continue
    x=SA[ri-1]
    while S[i+j]==S[x+j]:
      j+=1
    lcp[ri]=j
    if j:j-=1
  print(*(i+1 for i in SA))
  print(*lcp)
sol()
