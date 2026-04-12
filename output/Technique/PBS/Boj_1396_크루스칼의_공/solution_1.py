def find(x):
  if p[x]<0:return x
  p[x]=find(p[x])
  return p[x]

def union(x,y):
  a=find(x);b=find(y)
  if a==b:return p[b]
  if p[a]>p[b]:a,b=b,a
  p[a]+=p[b]
  p[b]=a
  return p[b]

n,m=map(int,input().split())

A=sorted([[*map(int,input().split())] for i in range(m)],key=lambda x:x[2])

q=int(input())
Q=[[0,1000001,[[*map(int,input().split())]+[i]for i in range(q)]]]
num=[-1]*q
p=[-1]*(n+1)

for i in range(20):
  for _ in range(n+1):p[_]=-1 #reset

  temp=[]
  i=0
  for T in Q:
    t1=[]
    t2=[]
    mid=T[0]+T[1]>>1

    while i<m:
      if A[i][2]>=mid:break
      union(A[i][0],A[i][1])
      i+=1

    for x,y,id in T[2]:
      if find(x)==find(y):
        t1.append([x,y,id])
        num[id]=-union(x,y)
      else:t2.append([x,y,id])

    if t1:temp.append([T[0],mid,t1])
    if t2:temp.append([mid,T[1],t2])

  Q=temp

for T in Q:
  for x,y,id in T[2]:
    if num[id]>=0:num[id]=(T[0],num[id])
    else:num[id]=[-1]

for k in num:print(*k)
