import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []

def solution4():
    
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    for i in numbers:
        if i not in answer:
            answer.append(i)
            solution4()
            answer.pop()
            
if __name__ == "__main__":
    solution4()