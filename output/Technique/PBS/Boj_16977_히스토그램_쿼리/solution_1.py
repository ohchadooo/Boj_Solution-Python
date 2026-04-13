def up(i,a):  #(maximum length,left side,right side):
  i+=s
  k=1
  st[i]=a
  i>>=1

  while i:
    x,y,z=st[2*i]
    w,e,r=st[2*i+1]
    if x==k:st[i][1]=k+e
    else:st[i][1]=y
    if w==k:st[i][2]=k+z
    else:st[i][2]=r
    st[i][0]=max(x,w,z+e)

    i>>=1
    k<<=1


def qu(i,j):
  i+=s;j+=s
  a=b=c=e=f=0
  k=1

  while i<j:
    if i&1:
      a=max(a,c+st[i],st[i][0])
      if st[i][0]==k:c+=k
      else:c=st[i][2]
      i+=1

    if not j&1:
      a=max(a,e+st[j][2],st[j][0])
      if st[j][0]==k:e+=k
      else:e=st[j][1]
      j-=1

    i>>=1;j>>=1
    k<<=1

  if i==j:
    if st[i][0]==k:a=max(a,c+k+e)
    else:a=max(a,c+st[i][1],e+st[i][2],st[i][0])

  else:a=max(a,c+e)

  return a

def pbs(cand):
  j=0
  temp=[]

  for i in range(s):up(i,[1,1,1])  #init

  for f,g,o in cand:
    if f+1==g:
      for w in o:ans[w[0]]=B[f][1]
      continue

    m=(f+g)>>1
    temp2=[[],[]]

    while j<m:
      up(B[j][0],[0,0,0])
      j+=1
    for w in o:
      if qu(w[1]-1,w[2]-1)>=w[3]:temp2[1].append(w)
      else:temp2[0].append(w)

    if temp2[0]:
      temp.append([f,m,temp2[0]])
    if temp2[1]:
      temp.append([m,g,temp2[1]])

  if temp:pbs(temp)

n=int(input())

A=[*map(int,input().split())]
B=sorted(enumerate(A),key=lambda x:x[1])

s=1
while s<=n:s<<=1
st=[[0,0,0]for i in range(s<<1)]

q=int(input())

Q=[[i]+[*map(int,input().split())]for i in range(q)]
ans=[0]*q

pbs([[0,n,Q]])
print(*ans)
