import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []

def solution7(n):
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return

    for i in range(n, N):
        answer.append(numbers[i])
        solution7(i)
        answer.pop()

    
if __name__ == "__main__":
    solution7(0)