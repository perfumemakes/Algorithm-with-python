import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []

def solution6():
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return

    for i in range(0, N):
        answer.append(numbers[i])
        solution6()
        answer.pop()
        
if __name__ == "__main__":
    solution6()