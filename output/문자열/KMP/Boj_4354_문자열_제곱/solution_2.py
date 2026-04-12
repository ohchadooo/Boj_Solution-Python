while (a:=input())!=".":
  k=(">"+a[:1]+a).find(a)
  print(len(a)//k)
