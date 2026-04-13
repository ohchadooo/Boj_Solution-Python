def f(x,y):return y[0]-x[0],y[1]-x[1]
def g(x,y):return x[0]*y[1]-x[1]*y[0]
def h(x):
  for n in range(-3,0):
    if T*g(f(A[n],A[n+1]),f(A[n],x))<0:return
  global cnt;cnt+=1

A=[[*map(int,input().split())]for i in range(3)]
x=g(f(A[0],A[1]),f(A[0],A[2]))
T=1
if x<0:x=-x;T=-1
print(x/2)

cnt=0
for i in range(int(input())):
  h(tuple(map(int,input().split())))
print(cnt)
