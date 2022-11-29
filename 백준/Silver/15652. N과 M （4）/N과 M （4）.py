import sys

input = sys.stdin.readline
N, M = map(int, input().split())
answer = []

def solution3(n):
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(n, N+1):
        answer.append(i)
        solution3(i)
        answer.pop()
    
if __name__ == "__main__":
    solution3(1)