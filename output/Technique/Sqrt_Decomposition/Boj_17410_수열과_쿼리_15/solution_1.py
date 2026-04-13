import sys
input = sys.stdin.readline

from bisect import bisect as R

n=int(input())
A=[*map(int,input().split())]
sq=int(n**0.5)

B=[sorted(A[i*sq:(i+1)*sq]) for i in range(n//sq+1)]

def qu1(x,y):
  x-=1;X=B[x//sq]
  i,j=R(X,A[x]),R(X,y)
  if i<j:
    for p in range(i,j):X[p-1]=X[p]
    X[j-1]=y
  elif i>j:
    for p in range(i-1,j-1,-1):X[p]=X[p-1]
    X[j]=y
  if i==j:X[i-1]=y
  A[x]=y

def qu2(i,j,k):
  i-=1;j-=1
  cnt=0

  if i//sq!=j//sq:
    for p in range(i,(i//sq+1)*sq):cnt+=A[p]>k
    for p in range(j//sq*sq,j+1):cnt+=A[p]>k
  else:
    for p in range(i,j+1):cnt+=A[p]>k
  for p in range(i//sq+1,j//sq):cnt+=sq-R(B[p],k)
  print(cnt)

for i in range(int(input())):
  a,*b=map(int,input().split())
  if a==1:qu1(*b)
  else:qu2(*b)
