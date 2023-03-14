def solution(n):
    if n % 2 == 0:
        n -= 1
    answer = []
    
    while n > 0:
        answer.append(n)
        n-=2
    answer=sorted(answer)
    return answer