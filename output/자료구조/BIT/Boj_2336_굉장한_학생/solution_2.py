input_data = """\
5 2 2
1
2
3
4
5
1 3 4 6
2 2 5
1 1 3 -2
2 2 5
"""

import sys
from io import StringIO

sys.stdin = StringIO(input_data)

import sys
input = sys.stdin.readline

def up(a,i,v):
  while i<n:
    a[i]+=v
    i+=i&-i

def rup(i,j,v):
  up(a1,i,v)
  up(a1,j+1,-v)
  up(a2,i,(-i+1)*v)
  up(a2,j+1,j*v)

def su(i):
  r=0;s=i
  while i:
    r+=a1[i]
    i-=i&-i
  r*=s
  while s:
    r+=a2[s]
    s-=s&-s
  return r

def q(i,j):return su(j)-su(i-1)

n,m,k=map(int,input().split())
n+=1

a1=[0]*n
a2=[0]*n

for i in range(1,n):
  up(a2,i,int(input()))

for i in range(m+k):
  a,*b=map(int,input().split())
  if a<2:rup(*b)
  else:print(q(*b))
