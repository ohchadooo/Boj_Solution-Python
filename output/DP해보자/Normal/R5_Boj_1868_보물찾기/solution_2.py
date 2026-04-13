import sys
#input=sys.stdin.readline
sys.setrecursionlimit(100000)

def len(x):
  cnt=-1
  while x:
    cnt+=1
    x>>=1
  return cnt

def dp(x=1): #top-down
  offs=[]
  nvis[x]=0
  for i in tree[x]:
    if nvis[i]:offs.append(dp(i)+1)

  if offs==[]:return 1
  offs.sort()

  M=offs.pop()
  while offs:
    M=merge(M, offs.pop())
  return M

def merge(x,y):
  m=x&y
  T=0
  if m:t=1<<len(m)
  else:t=max(x&-x,y&-y)

  if x&(t-1) or y&(t-1):T=1

  x&=~(2*t-1)
  y&=~(2*t-1)

  if T:t<<=1
  return t+x+y

n=int(input())
tree=[[]for i in range(n+1)]  # head: 1

for i in range(n-1):
  a,b=map(int,input().split())
  tree[a]+=b,
  tree[b]+=a,

nvis=[1]*(n+1)
print(len(dp()))
