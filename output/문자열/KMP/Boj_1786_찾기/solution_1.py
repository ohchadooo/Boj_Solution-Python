input_data = """\
ABC ABCDAB ABCDABCDABDE
ABCDABD
"""

import sys
from io import StringIO

sys.stdin = StringIO(input_data)

import sys
input = sys.stdin.readline

T=input().rstrip()
P=input().rstrip()

n=len(P)
pi=[0]

j=0
for i in range(1,n):
  while j and P[i]!=P[j]:
    j=pi[j-1]

  if P[i]==P[j]:j+=1
  pi+=j,

i=j=0;m=len(T)
c=0;ans=[]
while i<m:

  while j<n and i+j<m and T[i+j]==P[j]:
    j+=1

  if j==0:i+=1;continue
  if j==n:c+=1;ans+=i+1,

  i+=j-pi[j-1]
  j=pi[j-1]

print(c)
print(*ans)
