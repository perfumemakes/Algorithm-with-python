import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [0]*N
answer = []

def solution8():
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    check = 0
    for i in range(0, N):
        if not visited[i] and check != numbers[i]:
            visited[i] = 1
            answer.append(numbers[i])
            check = numbers[i]
            solution8()
            visited[i] = 0
            answer.pop()
            
solution8()