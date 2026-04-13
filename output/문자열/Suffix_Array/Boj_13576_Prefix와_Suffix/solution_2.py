#kmp

S=input()
n=len(S)
pi=[0]*n
for i in range(1,n):
  j=pi[i-1]
  while j and S[i]!=S[j]:j=pi[j-1]
  if S[i]==S[j]:j+=1
  pi[i]=j

ans=[]
j=n
while j:
  ans.append(j)
  j=pi[j-1]

cnt=[0]*(n+1)
for i in pi:cnt[i]+=1
for i in range(n-1,0,-1):cnt[pi[i-1]]+=cnt[i]

print(len(ans))
for i in reversed(ans):print(i,cnt[i]+1)
