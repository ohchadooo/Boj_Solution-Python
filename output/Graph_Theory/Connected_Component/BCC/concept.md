standard bcc



```
## bcc with cuts
def dfs(v,p):
  global k
  dfo[v]=low[v]=k
  k+=1
  ch=0
  for i in g[v]:
    if dfo[i]:
      if i!=p and dfo[i]<dfo[v]:
        st.append((v,i))
        if low[v]>dfo[i]:low[v]=dfo[i]
      continue
    if p==-1:ch+=1
    st.append((v,i))
    dfs(i,v)
    if low[v]>low[i]:low[v]=low[i]

    if low[i]>=dfo[v]:
      tmp=[]
      while True:
        x=st.pop()
        tmp.append(x)
        if x==(v,i):break

      if p!=-1:cut[v]=1
      bcc.append(tmp)

  if p==-1 and ch>1:cut[v]=1

st=[];bcc=[]
dfo=[0]*n
low=[0]*n
cut=[0]*n
```
