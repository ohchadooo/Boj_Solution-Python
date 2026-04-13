from functools import cmp_to_key as ckey
def d(x,y):return y[0]-x[0],y[1]-x[1]
def f(x,y):return x[0]*y[1]-x[1]*y[0]
def cmp(x,y):
  a=f(x,y)
  if a<0:return 1
  if a>0:return -1
  if x[0]**2+x[1]**2>y[0]**2+y[1]**2:return 1
  return -1

n,*X=map(int,input().split())
A=[[*map(int,input().split())]for i in range(n)]

cnt=0
while len(A)>2:
  temp=[]

  O=min(A)[:]
  for i in range(len(A)):A[i][0]-=O[0];A[i][1]-=O[1]
  X[0]-=O[0];X[1]-=O[1]
  A.sort(key=ckey(cmp))

  st=A[:2]
  for i in range(2,len(A)):
    while len(st)>1 and f(d(st[-2],st[-1]),d(st[-1],A[i]))<=0:
      if f(d(st[-2],st[-1]),d(st[-1],A[i]))<0:temp.append(st.pop())
      else:st.pop()
    st.append(A[i])

  for i in range(-1,len(st)-1):
    if f(d(st[i],st[i+1]),d(st[i+1],X))<=0:st=[];break
  if len(st)<3:break

  cnt+=1
  A=temp

print(cnt)
