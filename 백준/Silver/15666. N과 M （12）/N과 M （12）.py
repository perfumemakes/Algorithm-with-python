import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []

def solution11(n):
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    check = 0
    for i in range(n, N):
        if check != numbers[i]:
            answer.append(numbers[i])
            check = numbers[i]
            solution11(i)
            answer.pop()
            
if __name__ == "__main__":
    solution11(0)