a=int(input())
a1=list(map(int,input().split()))
b1=sum(a1[0:a:2])
b2=sum(a1[1:a:2])
d=b1-b2
print(abs(d))