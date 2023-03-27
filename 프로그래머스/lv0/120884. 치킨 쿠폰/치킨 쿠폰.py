def solution(chicken):
    answer = 0
    m = 0
    n = 0
    while chicken >= 10:
        m = chicken//10
        n = chicken%10
        chicken = m+n
        answer+= m
        
    return answer