n=int(input())

a=[1]*n
a1=[1]*(2*n-1)
a2=[1]*(2*n-1)

cnt=0

def backt(i=0):  # 가로축에 대해서만 정렬해줘도 중복 모두 제거됨
  global cnt
  if i==n:cnt+=1;return
  for j in range(n):
    if a[j] and a1[i+j] and a2[i-j]:
      a[j]=a1[i+j]=a2[i-j]=0
      backt(i+1)
      a[j]=a1[i+j]=a2[i-j]=1

backt()
print(cnt)
