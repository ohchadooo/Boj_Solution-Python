n=int(input())-2
a,b=map(int,input().split())
x,y=map(int,input().split())
x-=a;y-=b
r=0
for i in range(n):
  z,w=map(int,input().split())
  z-=a;w-=b
  r+=x*w-y*z
  x,y=z,w
print(abs(r/2))
