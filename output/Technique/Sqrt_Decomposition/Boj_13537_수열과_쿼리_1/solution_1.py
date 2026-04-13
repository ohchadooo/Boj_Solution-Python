import sys
input = sys.stdin.readline

from bisect import bisect as R

def sol():
  n=int(input())
  A=[*map(int,input().split())]
  sq=int(n**0.5)

  B=[sorted(A[i:i+sq]) for i in range(0,n,sq)]

  for i in range(int(input())):
    i,j,k=map(int,input().split())
    i-=1;j-=1
    cnt=0

    if i//sq!=j//sq:
      for p in range(i,(i//sq+1)*sq):cnt+=A[p]>k
      for p in range(j//sq*sq,j+1):cnt+=A[p]>k
    else:
      for p in range(i,j+1):cnt+=A[p]>k
    for p in range(i//sq+1,j//sq):cnt+=sq-R(B[p],k)

    print(cnt)

sol()
