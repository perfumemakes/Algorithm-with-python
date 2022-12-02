import sys

input = sys.stdin.readline

N,S = map(int,(input().split()))
numbers = list(map(int, input().split()))
cnt = 0

def solution(idx, target):
    global cnt
    
    if idx>=N:
        return
    target+=numbers[idx]
    
    if target==S:
        cnt+=1
        
    solution(idx+1, target)
    
    solution(idx+1, target-numbers[idx])
    

solution(0,0)
print(cnt)