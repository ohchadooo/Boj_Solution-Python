#kmp

n=int(input())
a=input()

pi=[0]*n

j=0
for i in range(1,n):
  while j and a[i]!=a[j]:
    j=pi[j-1]

  if a[i]==a[j]:j+=1
  pi[i]=j

print(n-pi[n-1])
