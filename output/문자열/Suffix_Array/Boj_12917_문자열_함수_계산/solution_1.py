t=input()
n=len(t);m=max(n,200)+1

r=[ord(i) for i in t]+[0]*n
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
  for i in range(n-k,n):nr[i-n+k]=i
  p=k
  for i in sa:
    if i>=k:
      nr[p]=i-k
      p+=1

  C[:m]=[0]*m
  for i in range(n):C[r[i]]+=1
  for i in range(m-1):C[i+1]+=C[i]
  for i in range(n-1,-1,-1):
    C[r[nr[i]]]-=1
    sa[C[r[nr[i]]]]=nr[i]

  nr,r=r,nr
  r[sa[0]]=1
  for i in range(1,n):
    a,b=sa[i],sa[i-1]
    r[a]=r[b]+((nr[a],nr[a+k])!=(nr[b],nr[b+k]))

  if r[sa[-1]]==n:break
  m=r[sa[-1]]+1
  k<<=1

t+="."
j=0;lcp=[0]*n
for i in range(n):
  if r[i]<2:continue
  x=sa[r[i]-2]
  while t[i+j]==t[x+j]:j+=1
  lcp[r[i]-2]=j
  if j:j-=1

st=[]
M=n
for i in range(n):
  while st and lcp[st[-1][0]]>=lcp[i]:
    l,j=st.pop()
    x=lcp[l]*(i-j+1)
    if M<x:M=x
  if st:st.append((i,st[-1][0]+1))
  else:st.append((i,0))

print(M)
