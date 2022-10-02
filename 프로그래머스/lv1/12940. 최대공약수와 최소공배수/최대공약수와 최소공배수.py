def solution(n, m):
    num=min(n,m)
    
    for i in range(num, 0, -1):
        if (n%i==0) and (m%i==0):
            break
    q=i
            
    answer = [q, n*m/q]
    return answer