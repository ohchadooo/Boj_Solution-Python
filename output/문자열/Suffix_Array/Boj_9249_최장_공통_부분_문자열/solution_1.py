A=input()
B=input()

n=len(A);m=len(B)
N=n+m
r=[ord(i)for i in A]+[-1]*N+[ord(i)for i in B]+[-1]*N
sv1=r[:]
nr=[-1]*(2*N+n+m)

sa=list(range(n))+list(range(n+N,n+m+N))
sv2=sa[:]

k=1
while k<N:
  sa.sort(key=lambda x:(r[x],r[x+k]))
  nr[sa[0]]=0
  for i in range(1,N):
    a,b=sa[i],sa[i-1]
    nr[a]=nr[b]+((r[a],r[a+k])!=(r[b],r[b+k]))
  nr,r=r,nr
  k<<=1

for i in range(N):
  r[sa[i]]=i

M=j=0;opt=0
for i in sv2:
  if r[i]<1:continue
  x=sa[r[i]-1]
  if (i-n)*(x-n)>0:continue
  while sv1[x+j]==sv1[i+j]!=-1:j+=1
  if M<j:M=j;opt=i
  if j:j-=1

print(M)
if M:
  if opt>=n:print(B[opt-N-n:opt-N-n+M])
  else:print(A[opt:opt+M])
