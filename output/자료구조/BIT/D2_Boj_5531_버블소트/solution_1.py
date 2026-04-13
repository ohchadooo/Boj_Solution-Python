def up(i,a):
  while i<=n:
    bit[i]+=a
    i+=i&-i

def query(i):
  res=0
  while i>0:
    res+=bit[i]
    i-=i&-i
  return res

def sum(i,j):
  return query(j-1)-query(i-1)

def dnc(s,e,p,q):
  global ans
  if s==e:return -1

  m=(s+e)>>1
  m_i=inc[m]
  M=-1

  st=max(m_i,p)

  for i in range(st,q):
    up(c[L[i]],1)
    if i==m_i:x=-1
    else:
      x=-1+sum(c[L[i]]+1,c[L[m_i]])+sum(c[L[i]],c[L[m_i]]+1)
    if x>=M:opt=i;M=x

  ans=max(ans,M)

  if e!=m+1:
    m2=inc[(m+1+e)//2]
    for i in range(max(opt,m2),q):
      up(c[L[i]],-1)  # BIT: m_i~opt-1

    for i in range(m_i,m2):
      up(c[L[i]],-1)  # BIT: m'_i~opt-1

    dnc(m+1,e,opt,q)

    #recover
    for i in range(max(opt,m2),q):
      up(c[L[i]],1)

    for i in range(m_i,m2):
      up(c[L[i]],1)


  if m!=s:
    m2=inc[(s+m)//2]
    for i in range(m2,min(m_i,p)):up(c[L[i]],1)
    for i in range(st,q):up(c[L[i]],-1)

    dnc(s,m,p,opt+1)

    for i in range(m2,min(m_i,p)):up(c[L[i]],-1)
    for i in range(st,q):up(c[L[i]],1)

  for i in range(st,q):
    up(c[L[i]],-1)

  return

def sol(n,a):
  global c,bit,inc,ans
  j=0
  c={i:(j:=j+1) for i in sorted(set(a))}

  if j<n:ans=0
  else:ans=-1

  inc=[0]
  for i in range(n-1):
    if a[inc[-1]]<a[i]:inc.append(i)

  bit=[0]*(n+1)

  res=0;N=0

  dnc(0,len(inc),0,n)
  res=-ans

  for x in a:
    res+=N-query(c[x])
    up(c[x],1);N+=1

  return res

n=int(input())
L=[int(input())for i in range(n)]
print(sol(n,L))
