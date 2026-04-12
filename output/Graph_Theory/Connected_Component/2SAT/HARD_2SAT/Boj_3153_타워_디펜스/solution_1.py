R,S=map(int,input().split())
Pic=[list(input().strip()) for i in range(R)]

F=[[[[]for k in range(4)]for j in range(S)]for i in range(R)]
B=[[[[]for k in range(4)]for j in range(S)]for i in range(R)]
for i in range(R):
  for j in range(S):
    if Pic[i][j]=='T':
      x=i+1
      while x<R and Pic[x][j]!='#':
        if Pic[x][j]=='T':
          F[i][j][0].append((i,j,3));F[x][j][3].append((x,j,0))
          B[i][j][3].append((i,j,0));B[x][j][0].append((x,j,3))
        x+=1
      x=j+1
      while x<S and Pic[i][x]!='#':
        if Pic[i][x]=='T':
          F[i][j][1].append((i,j,2));F[i][x][2].append((i,x,1))
          B[i][j][2].append((i,j,1));B[i][x][1].append((i,x,2))
        x+=1

for i in range(R):
  for j in range(S):
    if Pic[i][j]=='n':
      a=b=0
      x=i-1
      while x>=0 and Pic[x][j]!='#':
        if Pic[x][j]=='T':
          a=x,j,0
          break
        x-=1
      x=i+1
      while x<R and Pic[x][j]!='#':
        if Pic[x][j]=='T':
          if a!=0:a=0
          else:a=x,j,3
          break
        x+=1
      x=j-1
      while x>=0 and Pic[i][x]!='#':
        if Pic[i][x]=='T':
          b=i,x,1
          break
        x-=1
      x=j+1
      while x<S and Pic[i][x]!='#':
        if Pic[i][x]=='T':
          if b!=0:b=0
          else:b=i,x,2
          break
        x+=1

      if a==0 or b==0:
        if a==0:q,w,e=b
        else:q,w,e=a
        F[q][w][3-e].append((q,w,e))
        B[q][w][e].append((q,w,3-e))

      else:
        q,w,e=a
        r,t,y=b
        F[q][w][3-e].append((r,t,y));F[r][t][3-y].append((q,w,e))
        B[r][t][y].append((q,w,3-e));B[q][w][e].append((r,t,3-y))

def FD(i,j,k):
  nv[i][j][k]=0
  for x,y,z in F[i][j][k]:
    if nv[x][y][z]:FD(x,y,z)
  ST.append((i,j,k))

def BD(i,j,k):
  nv[i][j][k]=1
  if k in [0,3]:p=0
  else:p=1
  if Pic[i][j][p]==-1:Pic[i][j][p]=k>>1
  for a,b,c in B[i][j][k]:
    if nv[a][b][c]<1:BD(a,b,c)

nv=[[[1]*4 for j in range(S)]for i in range(R)]
ST=[]
for i in range(R):
  for j in range(S):
    if Pic[i][j]!="T":continue
    Pic[i][j]=[-1,-1]
    for k in range(4):
      if nv[i][j][k]:FD(i,j,k)

while ST:
  x,y,z=ST.pop()
  if nv[x][y][z]<1:BD(x,y,z)

for i in Pic:
  a=''
  for j in i:
    if type(j)==list:j=['4','1','3','2'][j[0]+j[1]*2]
    a+=j

  print(a)
