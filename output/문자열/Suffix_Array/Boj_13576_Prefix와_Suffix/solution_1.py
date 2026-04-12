#suffix array

S=input()
n=len(S);m=max(n,256)+1

r=[ord(i) for i in S]+[0]*n
if n==1:r[0]=1
nr=[0]*(2*n)
sa=[0]*n

C=[0]*m
for i in range(n):C[r[i]]+=1
for i in range(m-1):C[i+1]+=C[i]
for i in range(n-1,-1,-1):
  C[r[i]]-=1
  sa[C[r[i]]]=i

k=1
while k<n:
  for i in range(n-k,n):nr[i+k-n]=i
  p=k
  for i in sa:
    if i>=k:
      nr[p]=i-k
      p+=1

  C[:m]=[0]*m
  for i in range(n):C[r[i]]+=1
  for i in range(m-1):C[i+1]+=C[i]
  for i in range(n-1,-1,-1):
    x=nr[i]
    C[r[x]]-=1
    sa[C[r[x]]]=x

  r,nr=nr,r
  r[sa[0]]=1
  for i in range(1,n):
    a,b=sa[i],sa[i-1]
    r[a]=r[b]+((nr[a],nr[a+k])!=(nr[b],nr[b+k]))

  if r[sa[-1]]==n:break
  m=r[a]+1
  k<<=1

S+=".";lcp=[0]*n
j=0
for i in range(n):
  if r[i]<2:continue
  x=sa[r[i]-2]
  while S[i+j]==S[x+j]:j+=1
  lcp[r[i]-1]=j
  if j:j-=1

x=r[0]

t=n
cand=[[n,1]]
for i in range(r[0]-1,0,-1):
  if t>lcp[i]:t=lcp[i]
  if t==0:break
  if sa[i-1]+t==n:cand.append([t,x-i+1])

sv=x
for i in range(len(cand)):
  while x<n and lcp[x]>=cand[i][0]:x+=1
  cand[i][1]+=x-sv

print(len(cand))
for i in reversed(cand):print(*i)
