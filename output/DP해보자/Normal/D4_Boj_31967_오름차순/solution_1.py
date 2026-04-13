n,q=map(int,input().split())
A=[*map(int,input().split())]

t=[0]
x=A[0]
for i in range(1,n):
  k=0
  y=A[i]
  if x>=y:
    while x>y<<k:k+=1
  else:
    while x<<k<=y:k+=1
    k=-k+1
  t.append(k)
  x=y

Q=[[*map(int,input().split())]+[i]for i in range(q)]
Q.sort(key=lambda x:x[1])

S=[0]
for i in range(1,n):
  S.append(S[-1]+t[i])

connec=[n]*n
stack=[0]
for i in range(1,n):
  while stack:
    if S[stack[-1]]>S[i]:
      connec[stack.pop()]=i
      ##
    else:break
  stack.append(i)


memo=[0]*n

SS=[0]
for i in range(1,n):
  SS.append(SS[-1]+S[i])


def query(i,j):
  return SS[j]-SS[i]-(j-i)*S[i]

def comp(a,b):
  x=connec[a]
  if x>b:return query(a,b),a

  p,q=comp(x,b)
  memo[a]=query(a,x-1)+p

  return memo[a],q  # 누적S합,압축경로


ans=[0]*q
for a,b,i in Q: #a,b값은 리스트 좌표보다 1크다.
  pp,qq=comp(a-1,b-1)
  ans[i]=pp

print(*ans)
