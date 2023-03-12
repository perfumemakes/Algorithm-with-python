def solution(n):
    answer = 0
    if n%2 == 0:
        answer += n
        
        while n>0:
            n -= 2
            answer += n
        
        return answer
    else:
        n -= 1
        answer += (n)
        
        while n>0:
            n -= 2
            answer += n
        
        return answer