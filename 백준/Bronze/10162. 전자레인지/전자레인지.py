import sys
input=sys.stdin.readline
n=int(input())

x=300
y=60
z=10


a=n//x
b=(n-(a*x))//y
c=(n-(a*x)-(b*y))//z

if (n-(a*x)-(b*y))%z != 0:
    print(-1)
else:
    print(a, b, c)