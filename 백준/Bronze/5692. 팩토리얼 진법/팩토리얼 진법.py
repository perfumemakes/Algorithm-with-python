import sys

def func(x):
    if x>1:
        return x*func(x-1)
    else:
        return 1

while True:
    num=sys.stdin.readline().strip()
    if(num=='0'):
        break
    else:
        num=list(num)
        length=len(num)
        sum=0
        for i in range(length):
            sum+=int(num[i])*func(length-i)
    print(sum)
    