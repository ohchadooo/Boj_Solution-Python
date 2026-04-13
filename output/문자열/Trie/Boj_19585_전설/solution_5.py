n,*s=map(int,input().split())
st=[]
c=0
suc=0
for i in s:
  while st and st[-1]<i:
    st.pop()
    c+=1
  if st:
    if st[-1]==i:suc+=1
    else:suc=1
    c+=suc
  else:suc=0
  st.append(i)
print(c)
