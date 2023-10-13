a=int(input())
a1=list(map(int,input().split()))
s=sum(a1)
avg=s//a
print(avg in a1)