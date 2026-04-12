def FD(i):
  T[i]=0
  for j in F[i]:
    if T[j]:FD(j)
  S.append(i)
def FF(i):
  nS.append(i)
  T[i]=1
  for j in F[i]:
    if T[j]==0:FF(j)
def BD(i):
  T[i]=-1
  for j in B[i]:
    if T[j]>0:BD(j)
  nap[-1][-1]+=1
n,k=map(int,input().split())
a=[*map(int,input().split())]
F=[[]for i in range(n)]
B=[[]for i in range(n)]
for i in range(n):
  F[a[i]-1].append(i)
  B[i].append(a[i]-1)
T=[1]*n
S=[]
for i in range(n):
  if T[i]:FD(i)
nS=[]
nap=[]
while S:
  i=S.pop()
  if T[i]==0:
    FF(i)
    nap.append([])
    for j in nS:
      if T[j]>0:
        nap[-1].append(0)
        BD(j)
    nap[-1].reverse()
    i=nap[-1]
    for j in range(len(i)-1):
      i[j+1]+=i[j]
N=1
for i in nap:
  s=N
  for j in i:
    N|=s<<j
N>>=(n-k)
N&=-N
print(k+1-N.bit_length())
