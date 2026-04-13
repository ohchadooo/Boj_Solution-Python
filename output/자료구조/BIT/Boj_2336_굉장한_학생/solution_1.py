# 1번 시험 성적으로 정렬: i
# i=0부터 시작하여 매 i 마다 i-1 i>=0)의 정보를 트리에 저장
# i보다 시험을 잘본 ~i-1이 계속 저장될 거임

# 2번 시험: a_i, 3번 시험: b_i로 정렬되어 있으면
# 0~(a_i-1)에 해당하는 b_i의 최솟값 쿼리를 펜윅으로 구현
# 그럼 1,2번 모두 i보다 잘본 사람들 중 3번시험 등수의 최솟값이 나옴
# 최솟값<b_i면 i는 굉장한 학생

n=int(input())
L=[*map(int,input().split())]

a=[0]*(n+1);j=1
for i in map(int,input().split()):
  a[i]=j;j+=1

a=[0]*(n+1);j=1
for i in map(int,input().split()):
  a[i]=j;j+=1

inf=1e6
T=[inf]*(n+1)

def up(t,i):
  while i<=n:
    T[i]=min(t,T[i])
    i+=i&-i

def qu(i):
  res=inf
  while i>0:
    res=min(T[i],res)
    i-=i&-i
  return res

cnt=1
for i in range(n-1):
  up(a[L[i]],a[L[i]])
  x=qu(a[L[i+1]]-1)
  if x>a[L[i+1]]:cnt+=1

print(cnt)
