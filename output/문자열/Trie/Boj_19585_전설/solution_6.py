n,*s=map(int,input().split())
st=[]
c=0
suc=0
for i in s:
  while st and st[-1][0]<i:
    st.pop();c+=1
  b=0
  if st:
    if st[-1][0]==i:b=st[-1][1]+1
    else:b=1
    c+=b
  st.append((i,b))
print(c)
