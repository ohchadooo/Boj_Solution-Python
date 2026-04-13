input_data = """\
7
1 2
2 3
2 4
1 5
5 6
4 7
5
1 2 7
3 1 5
2 1 7
5 6 2
6 2 3
"""

import sys
from io import StringIO

sys.stdin = StringIO(input_data)

import sys
input = sys.stdin.readline

s=int(input())
n=s+1;k=0
while s:s>>=1;k+=1

g=[[]for i in range(n)]
for i in range(n-2):
  a,b=map(int,input().split())
  g[a]+=b,;g[b]+=a,

P=[[0]*n for i in range(k)];P[0][1]=1
D=[0]*n
st=[1]

while st:
  i=st.pop()
  for j in g[i]:
    if P[0][i]==j:continue
    st+=j,
    D[j]=D[i]+1
    P[0][j]=i

for j in range(k-1):
  for i in range(1,n):
    P[j+1][i]=P[j][P[j][i]]

def f(a,b):
  if D[a]<D[b]:a,b=b,a
  dd=D[a]-D[b]
  for j in range(k):
    if dd&(1<<j):a=P[j][a]

  if a==b:return a
  for j in range(k-1,-1,-1):
    if P[j][a]!=P[j][b]:
      a=P[j][a];b=P[j][b]

  return P[0][a]

for _ in range(int(input())):
  t=[*map(int,input().split())]
  tt=[]
  for i in range(-1,2):
    tt+=f(t[i],t[i+1]),

  mn=tt[2]
  for i in range(2):
    if D[tt[i]]>D[mn]:mn=tt[i]

  print(mn)
