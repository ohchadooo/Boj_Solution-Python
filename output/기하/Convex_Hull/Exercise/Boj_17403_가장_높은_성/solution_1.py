from functools import cmp_to_key as ckey
def cp(x,y):return x[0]*y[1]-x[1]*y[0]
def vec(x,y):return y[0]-x[0],y[1]-x[1]
def cmp(x,y):
  a=cp(x,y)
  if a<0:return 1
  if a>0:return -1
  if x[0]**2+x[1]**2>y[0]**2+y[1]**2:return 1
  return -1
n=int(input())
flr=[0]*n
k=m=0
B=[[*map(int,input().split())]+[i] for i in range(n)]
while k<n:
  temp=[]
  S=min(B)[:]
  for i in B:i[0]-=S[0];i[1]-=S[1]
  B.sort(key=ckey(cmp))
  st=B[:2]
  for i in range(2,len(B)):
    while len(st)>1 and cp(vec(st[-2],st[-1]),vec(st[-1],B[i]))<=0:
      temp.append(st.pop())
    st.append(B[i])
  if len(st)<3:break
  k+=len(st)
  m+=1
  for i in st:
    flr[i[2]]=m
  B=temp

print(*flr)
