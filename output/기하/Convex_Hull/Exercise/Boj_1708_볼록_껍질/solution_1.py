from functools import cmp_to_key as ckey
def f(x,y):return x[0]*y[1]-x[1]*y[0]
def vec(x,y):return y[0]-x[0],y[1]-x[1]
def cmp(x,y):
  a=f(x,y)
  if a<0:return 1
  if a>0:return -1
  if x[0]**2+x[1]**2>y[0]**2+y[1]**2:return 1  # 거리가 먼 점을 뒤쪽으로
  return -1
n=int(input())
A=[[*map(int,input().split())]for i in range(n)]
S=min(A)[:]

for i in A:i[0]-=S[0];i[1]-=S[1]
A.sort(key=ckey(cmp))

st=[A[0],A[1]]
for i in range(2,n):
  while (x:=f(vec(st[-2],st[-1]),vec(st[-1],A[i])))<0:st.pop()
  if x==0:st.pop()
  st.append(A[i])

print(len(st))
