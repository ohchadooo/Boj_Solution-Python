## S_j monotonically increases: O(n) technique

from collections import deque

n,k=map(int,input().split())
k+=1
S=[*map(int,input().split())]

for i in range(1,n):S[i]+=S[i-1]

dp=[i**2 for i in S]

track=[[0]*(n-k+1) for i in range(k-2)]

def J(a,b):
  if S[a]==S[b]:return 10**18
  return (dp[a]+S[a]**2-dp[b]-S[b]**2)//(2*(S[a]-S[b]))

def main():
  global dp
  temp=[0]*n
  for j in range(1,k):
    L=deque([j-1])
    for _ in range(n):temp[_]=0

    for i in range(n-k+1):
      while len(L)>1 and J(i+j-1,L[-1])<=J(L[-1],L[-2]):
        L.pop()

      L.append(i+j-1)

      while len(L)>1 and J(L[0],L[1])<S[i+j]:
        L.popleft()

      id=L[0]
      if j<k-1:track[j-1][i]=id
      #print(id,dp[id])
      temp[i+j]=(S[i+j]-S[id])**2+dp[id]

    for _ in range(n):dp[_]=temp[_]

  print((S[n-1]**2-dp[n-1])//2)

  an=[0]*(k-2)+[id+1]
  j-=1
  while j:
    id=track[j-1][id-j]
    j-=1
    an[j]=id+1
  print(*an)

main()
