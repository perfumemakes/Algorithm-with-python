import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []

def solution5(n):
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return

    for i in range(n, N):
        if numbers[i] not in answer:
            answer.append(numbers[i])
            solution5(i+1)
            answer.pop()

    
if __name__ == "__main__":
    solution5(0)