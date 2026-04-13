def f(a,b):
  if D[a]<D[b]:a,b=b,a
  dd=D[a]-D[b]
  for j in range(k):
    if dd&(1<<j):a=P[j][a]

  if a==b:return a
  for j in range(k-1,-1,-1):
    if P[j][a]!=P[j][b]:
      a=P[j][a];b=P[j][b]

  return P[0][a]

print(f(2,7))
