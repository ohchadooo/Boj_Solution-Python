r=30

n=int(input())
A=[*map(int,input().split())]
id=[[-1,-1]for i in range(n*r+3)]

vs=1
for i in A:
  cur=0
  for j in range(r,-1,-1):
    tf=(i>>j)&1
    if id[cur][tf]<0:
      id[cur][tf]=vs
      vs+=1

    cur=id[cur][tf]

M=0
for i in A:
  cur=xor=0
  for j in range(r,-1,-1):
    tf=(i>>j)&1
    if id[cur][1-tf]<0:tf=1-tf
    else:xor+=1<<j
    cur=id[cur][1-tf]
  if M<xor:M=xor

print(M)
