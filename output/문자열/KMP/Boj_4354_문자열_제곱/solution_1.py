inp="""\
abcd
aaaa
ababab
.
"""

import sys
from io import StringIO
sys.stdin=StringIO(inp)

import sys
input=sys.stdin.readline

while (a:=input())!=".":
  n=len(a)
  pi=[0]*n

  j=0
  for i in range(1,n):
    while j and a[i]!=a[j]:
      j=pi[j-1]
    if a[i]==a[j]:j+=1
    pi[i]=j

  k=n-j
  print(1 if n%k else n//k)
