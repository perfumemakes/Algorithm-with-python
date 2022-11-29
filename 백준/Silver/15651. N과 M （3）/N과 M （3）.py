import sys

input = sys.stdin.readline
N, M = map(int, input().split())
answer = []

def solution2():
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
        
    for i in range(1, N+1):
        answer.append(i)
        solution2()
        answer.pop()
        
solution2()