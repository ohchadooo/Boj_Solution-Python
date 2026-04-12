import sys
input = sys.stdin.readline

c,n=map(int,input().split())

col=[[0]*27];nick=[[0]*27]

uv=1
for i in range(c):
  cur=0
  for a in input().strip():
    id=ord(a)-ord("a")
    if col[cur][id]==0:
      col[cur][id]=uv
      uv+=1
      col.append([0]*27)
    cur=col[cur][id]
  col[cur][26]=1

uv=1
for i in range(n):
  cur=0
  for a in input().strip()[::-1]:
    id=ord(a)-ord("a")
    if nick[cur][id]==0:
      nick[cur][id]=uv
      uv+=1
      nick.append([0]*27)
    cur=nick[cur][id]
  nick[cur][26]=1


check=[-1]*2000
for i in range(int(input())):
  x=[ord(a)-ord("a") for a in input().strip()]
  l=len(x)

  cur=T=0
  for j in range(l-1):
    if col[cur][x[j]]==0:break
    cur=col[cur][x[j]]
    if col[cur][26]:check[j+1]=i

  cur=0
  for j in range(l-1,0,-1):
    if nick[cur][x[j]]==0:break
    cur=nick[cur][x[j]]
    if nick[cur][26] and check[j]==i:T=1;break

  print(["No","Yes"][T])
