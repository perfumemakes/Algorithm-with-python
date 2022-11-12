import sys
from collections import deque
input = sys.stdin.readline

gear =[deque(list(map(int, input().rstrip()))) for _ in range(4)]

r = int(input())
for _ in range(r):
    arr=[]
    for i in range(4):
        arr.append([gear[i][6],gear[i][2]])
    n,d=map(int,input().split())
    n=n-1

    if n != 0:
        for i in range(n,0,-1):
            if arr[i][0] != arr[i-1][1]:
                if (n-(i-1))%2 == 0:
                    gear[i-1].rotate(d)
                elif (n-(i-1))%2 != 0:
                    gear[i-1].rotate(-d)
            elif arr[i][0] == arr[i-1][1]:
                break
    if n != 3:
        for i in range(n,3):
            if arr[i][1] != arr[i+1][0]:
                if (n-(i+1))%2 == 0:
                    gear[i+1].rotate(d)
                elif (n-(i+1))%2 != 0:
                    gear[i+1].rotate(-d)
            elif arr[i][1] == arr[i+1][0]:
                break
    gear[n].rotate(d)
    
sum=gear[0][0] + gear[1][0]*2 + gear[2][0]*4 + gear[3][0]*8
print(sum)    