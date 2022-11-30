import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [0]*N
answer = []

def solution9(n):
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    check = 0
    for i in range(n, N):
        if not visited[i] and check != numbers[i]:
            visited[i] = 1
            answer.append(numbers[i])
            check = numbers[i]
            solution9(i+1)
            visited[i] = 0
            answer.pop()
        


if __name__ == "__main__":
    solution9(0)