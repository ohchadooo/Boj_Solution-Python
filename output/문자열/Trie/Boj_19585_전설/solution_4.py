n,*s=map(int,input().split())
st=[]
c=0
for i in s:
  while st and st[-1]<i:
    st.pop()
    c+=1
  if st:c+=1
  st.append(i)
  print(st,c)

print(c)
