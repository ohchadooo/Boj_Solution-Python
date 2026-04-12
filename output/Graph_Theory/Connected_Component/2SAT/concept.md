2SAT-Optimized Form



```
import sys
sys.setrecursionlimit(100000)
def FD(i):
  T[i]=0
  for j in F[i]:
    if T[j]:FD(j)
  S.append(i)
def BD(i):
  if T[-i]==x:global A;A=0;return
  T[i]=x
  for j in B[i]:
    if T[j]==0:BD(j)
def g():
  for i in range(m):
    a,b=map(int,input().split())
    F[-a]+=b,;F[-b]+=a,
    B[b]+=-a,;B[a]+=-b,
n,m=map(int,input().split())
k=2*n+1
F=[[]for i in range(k)]
B=[[]for i in range(k)]
g()
T=[1]*k
S=[]
for i in range(-n,n+1):
  if T[i]:FD(i)
T[0]=1  # 0 제거
A=1
while S:  #S and A 해도 됨
  x=S.pop()
  if T[x]==0:BD(x)
print(A)
```
