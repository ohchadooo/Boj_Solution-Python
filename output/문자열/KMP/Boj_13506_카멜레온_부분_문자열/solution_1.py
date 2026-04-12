S="qwertyqwertyqwerty"
n=len(S)

pi=[0]*n
j=0
for i in range(1,n):
  while j and S[j]!=S[i]:
    j=pi[j-1]
  if S[i]==S[j]:j+=1
  pi[i]=j

M=0
for i in range(n-1):
  if M<pi[i]:M=pi[i]

j=n-1
while 1:
  if j==0 or pi[j]==0:
    print(-1)
    break
  if M>=pi[j]:print(S[:pi[j]]);break
  j=pi[j]-1
