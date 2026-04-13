import sys
sys.setrecursionlimit(100000)

n=int(input())+1

FW=[[]for i in range(n)]
BW=[[]for i in range(n)]

for i in range(1,n):
  k=map(int,input().split())
  next(k)
  for j in k:
    FW[i].append(j)
    BW[j].append(i)

def FD(i):
  nv[i]=0
  for j in FW[i]:
    if nv[j]:FD(j)
  stack.append(i)

def BD(i):
  nv[i]=0
  SCC[-1].append(i)
  for j in BW[i]:
    if nv[j]:BD(j)

nv=[1]*n
stack=[]

for i in range(1,n):
  if nv[i]:FD(i)
for i in range(1,n):nv[i]=1

SCC=[]
while stack:
  i=stack.pop()
  if nv[i]:
    SCC.append([])
    BD(i)

for i in range(1,n):nv[i]=1

C=0
wh=[0]*n
ls=len(SCC)
for i in range(ls):
  for j in SCC[i]:
    wh[j]=i

cnt=[0]*ls

id=1
for _ in range(ls):
  if _==id:break
  X=SCC[_]
  cand=[]

  for i in X:
    for j in FW[i]:
      if cnt[wh[j]]==0:cand.append(wh[j])
      cnt[wh[j]]+=1

  k=ls-1
  while k>=id:
    if cnt[k]!=len(SCC[k])*len(SCC[_]):break
    k-=1

  k+=1
  id=k

  for i in cand:cnt[i]=0


ans=[]
for i in range(id):ans+=SCC[i]
ans.sort()
print(len(ans),*ans)
