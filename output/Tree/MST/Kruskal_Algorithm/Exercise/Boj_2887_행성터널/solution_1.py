n=int(input())
x=[];y=[];z=[]
for i in range(n):
  a,b,c=map(int,input().split())
  x.append((a,i))
  y.append((b,i))
  z.append((c,i))

kruskal=[]
for i in x,y,z:
  i.sort()
  for j in range(n-1):
    kruskal+=(i[j][0]-i[j+1][0],i[j][1],i[j+1][1]),

kruskal.sort()

# Union Find
p=[-1]*(n+1)

def find(x):
  if p[x]<0:return x
  p[x]=find(p[x])
  return p[x]

def union(x,y):
  a,b=find(x),find(y)
  if a==b:return 0
  if p[a]>p[b]:a,b=b,a
  p[a]+=p[b]
  p[b]=a
  return 1

ans=cnt=0
while cnt<n-1:  # (n-1) connecting
  a,b,c=kruskal.pop()
  if union(b,c):
    cnt+=1
    ans+=-a

print(ans)
