#포인터 이동 (버전 더 쉬움)

from itertools import chain
import sys
input=sys.stdin.readline

n=int(input())
sq=int(n**0.5)
A=[*map(int,input().split())]

Q=[]
for i in range(int(input())):
  Q.append(list(map(int,input().split()))+[i])

Q.sort(key=lambda x:(x[0]//sq,x[1]))

cnt=[0]*1000001
i=j=c=0

ans=[0]*len(Q)

for a,b,id in Q:
  a-=1
  if j<a:
    for p in range(i,j):cnt[A[p]]=0
    i=j=a;c=0

  for p in chain(range(i,a),range(b,j)):
    cnt[A[p]]-=1
    if cnt[A[p]]==0:c-=1

  for p in chain(range(a,i),range(j,b)):
    if cnt[A[p]]==0:c+=1
    cnt[A[p]]+=1

  i,j=a,b
  ans[id]=c

print(*ans)
