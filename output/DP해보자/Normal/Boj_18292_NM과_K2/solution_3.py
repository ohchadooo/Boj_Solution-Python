L=1<<10

TF=[1]*L

for i in range(L):
  j=3
  s=i
  while s:
    if s&j==j:TF[i]=0
    s>>=1
T=[i for i in range(L) if TF[i]]
print(len(T))
