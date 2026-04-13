from functools import cmp_to_key as ckey
from matplotlib import pyplot as plt
def f(x,y):return x[0]*y[1]-x[1]*y[0]
def vec(x,y):return y[0]-x[0],y[1]-x[1]
def cmp(x,y):
  p,q=vec(S,x),vec(S,y)
  a=f(p,q)
  if a<0:return 1
  if a>0:return -1
  if p[0]**2+p[1]**2>q[0]**2+q[1]**2:return 1
  return -1
n=8
A=[[1, 2], [1, 3], [2, 1], [1, 1], [2, 2], [2, 3], [3, 1], [3, 2]]
S=min(A)[:]

A.sort(key=ckey(cmp))

plt.scatter(*zip(*A),c='black',s=5)
for i in range(n):
  plt.text(A[i][0]+0.05,A[i][1]+0.05,i)

st=[A[0],A[1]]
for i in range(2,n):
  while (x:=f(vec(st[-2],st[-1]),vec(st[-1],A[i])))<0:st.pop()
  if x==0:st.pop()
  st.append(A[i])

st+=[st[0]]
plt.plot(*zip(*st),c='blue')
for i in range(len(st)-1):
   plt.text(st[i][0]+0.1,st[i][1]+0.06,i,c='blue')
plt.show()
