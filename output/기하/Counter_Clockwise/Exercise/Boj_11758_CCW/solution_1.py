def f(x,y):return y[0]-x[0],y[1]-x[1]
def g(x,y):
  a=x[0]*y[1]-x[1]*y[0]
  if a>0:return 1
  if a<0:return -1
  return 0

A=[[*map(int,input().split())]for i in range(3)]
print(g(f(A[0],A[1]),f(A[1],A[2])))
