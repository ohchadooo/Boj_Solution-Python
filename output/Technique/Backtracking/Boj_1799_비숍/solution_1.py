n,*A=map(int,input().split())

t1=[1]*n  #black diagonal
t2=[1]*(n-1)    #white diagonal

a=(n-1)>>1
b=n>>1

M1=M2=0

def back1(x=-a,k=0):
  global M1
  if k>M1:M1=k

  for i in range(x,a+1):
    pos=-2*n*i if i<0 else 2*i

    nu=n+2*i if i<0 else n-2*i
    T=nu>>1
    for j in range(nu):
      if t1[T-j] and A[pos+(n+1)*j]:
        t1[T-j]=0
        back1(i+1,k+1)
        t1[T-j]=1

def back2(x=-b,k=0):
  global M2
  if k>M2:M2=k

  for i in range(x,b):
    pos=-n*(2*i+1) if i<0 else 2*i+1

    nu=n+1+2*i if i<0 else n-1-2*i
    T=nu>>1
    for j in range(nu):
      if t2[T-j] and A[pos+(n+1)*j]:
        t2[T-j]=0
        #print(i,j,T,pos+(n+1)*j,t2)
        back2(i+1,k+1)
        t2[T-j]=1

back1();back2()
print(M1+M2)
