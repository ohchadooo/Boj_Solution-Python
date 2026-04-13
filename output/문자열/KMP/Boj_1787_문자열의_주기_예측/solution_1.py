n=int(input())
S=input()

pi=[0]*n
D=[0]*n
j=0
for i in range(1,n):
  while j and S[j]!=S[i]:
    j=pi[j-1]

  if S[j]==S[i]:j+=1
  pi[i]=j

  if j and D[j-1]:D[i]=D[j-1]
  else:D[i]=j if 2*j<=i+1 else 0

ans=0
for i in range(n):
  if D[i]:ans+=i+1-D[i]

print(ans)
