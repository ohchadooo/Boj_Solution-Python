n,m=map(int,input().split())

a=[]
T=[1]*n
def backt():
  if len(a)==m:print(*a);return
  for j in range(n):
    if T[j]:
      a.append(j+1)
      T[j]=0
      backt()
      a.pop()
      T[j]=1

backt()
