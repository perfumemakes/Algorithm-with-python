import sys
input = sys.stdin.readline

N,M = map(int, input().split())
answer = []

def solution(n):
    
    if len(answer)==M:
        print(" ".join(map(str, answer)))
    
    for i in range(n, N+1):
        if i not in answer:
            answer.append(i)
            solution(i+1)
            answer.pop()

solution(1)