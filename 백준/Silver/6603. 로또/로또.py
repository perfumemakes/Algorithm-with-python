import sys
input=sys.stdin.readline
answer = [0 for i in range(13)]

def solution(n,d):
    if d==6:
        for i in range(6):
            print(answer[i], end=' ')
        print()
        return
    for i in range(n, len(temp)):
        answer[d]=temp[i]
        solution(i+1, d+1)

while True:
    temp = list(map(int, input().split()))
    
    if temp[0]==0:
        break
    
    temp.pop(0)
    solution(0,0)
    print()
    