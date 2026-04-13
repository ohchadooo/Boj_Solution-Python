def sol():
  S=input()
  n=len(S)

  M=0
  pi=[0]*n
  for p in range(n-1):
    pi[p]=0
    j=p
    for i in range(p+1,n):
      while j>p and S[i]!=S[j]:
        j=pi[j-1]+p
      if S[i]==S[j]:
        j+=1
        if M<j-p:M=j-p
      pi[i]=j-p

  print(M)

sol()
